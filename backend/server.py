from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pathlib import Path
import csv,json,sqlite3,os
from datetime import datetime,timezone
from typing import Optional
from backend.app.services.ioc_validator import validate_indicator
from backend.app.services.enrichment_engine import enrich_indicator
from backend.app.services.risk_engine import calculate_vulnerability_priority
from backend.app.services.correlation_engine import correlate_threats
from backend.app.services.alert_engine import generate_threat_alert
from backend.app.utils.security import analyst_auth
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'; AWARE=ROOT/'awareness'; DB_PATH=Path(os.getenv('DATABASE_PATH',str(DATA/'threat_intelligence.db')))
app=FastAPI(title='Cybersecurity Awareness & Threat Intelligence Dashboard',version='1.0.0',description='Defensive, synthetic threat-intelligence and awareness platform.')
app.add_middleware(CORSMiddleware,allow_origins=os.getenv('CORS_ORIGINS','http://localhost:5173').split(','),allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
def db():
    con=sqlite3.connect(DB_PATH); con.row_factory=sqlite3.Row; return con
def init_db():
    DB_PATH.parent.mkdir(parents=True,exist_ok=True); con=db(); con.executescript('''CREATE TABLE IF NOT EXISTS threats(threat_id TEXT PRIMARY KEY,threat_name TEXT,category TEXT,description TEXT,severity TEXT,risk_score INTEGER,confidence_score INTEGER,status TEXT,first_seen TEXT,last_seen TEXT,indicator_type TEXT,indicator_value TEXT,source_name TEXT,source_reliability TEXT,mitre_tactic TEXT,mitre_technique TEXT,cve_id TEXT,campaign_id TEXT,observation_count INTEGER);CREATE TABLE IF NOT EXISTS analyst_notes(note_id INTEGER PRIMARY KEY AUTOINCREMENT,threat_id TEXT,note TEXT,created_at TEXT);CREATE TABLE IF NOT EXISTS alerts(alert_id TEXT PRIMARY KEY,threat_id TEXT,timestamp TEXT,alert_type TEXT,severity TEXT,risk_score INTEGER,confidence_score INTEGER,description TEXT,status TEXT);CREATE TABLE IF NOT EXISTS audit_log(id INTEGER PRIMARY KEY AUTOINCREMENT,action TEXT,target_id TEXT,old_value TEXT,new_value TEXT,created_at TEXT);'''); con.commit(); con.close()
def load_records():
    p=DATA/'threat_intelligence_dataset.csv'
    if not p.exists(): return []
    with p.open(encoding='utf-8') as f:return list(csv.DictReader(f))
def seed_db():
    rows=load_records(); con=db(); existing=con.execute('SELECT COUNT(*) c FROM threats').fetchone()['c']
    if existing==0 and rows:
        con.executemany('INSERT INTO threats VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[(r['threat_id'],r['threat_name'],r['threat_category'],r['description'],r['severity'],int(r['risk_score']),int(r['confidence_score']),r['status'],r['first_seen'],r['last_seen'],r['indicator_type'],r['indicator_value'],r['source_name'],r['source_reliability'],r['mitre_tactic_optional'],r['mitre_technique_optional'],r['cve_id_optional'],r['campaign_id'],int(r['observation_count'])) for r in rows]);
        for r in rows:
            rr=dict(r); rr['risk_score']=int(rr['risk_score']); rr['confidence_score']=int(rr['confidence_score']); a=generate_threat_alert(rr)
            if a: con.execute('INSERT OR IGNORE INTO alerts VALUES(?,?,?,?,?,?,?,?,?)',(a['alert_id'],a['threat_id'],a['timestamp'],a['alert_type'],a['severity'],a['risk_score'],a['confidence_score'],a['description'],a['status']))
        con.commit()
    con.close()
init_db(); seed_db()
class ThreatCreate(BaseModel):
    threat_name:str=Field(min_length=3,max_length=200); category:str; description:str=Field(min_length=1,max_length=2000); severity:str; risk_score:int=Field(ge=0,le=100); confidence_score:int=Field(ge=0,le=100); status:str='NEW'; indicator_type:str; indicator_value:str; source_name:str='Internal SOC'
class NoteCreate(BaseModel): note:str=Field(min_length=1,max_length=2000)
class AlertStatus(BaseModel): status:str
class QuizSubmit(BaseModel): answers:dict[str,int]
@app.get('/api/health')
def health():return {'status':'ok','mode':'SYNTHETIC / DEMO ONLY'}
@app.get('/api/dashboard/stats')
def stats():
    con=db(); total=con.execute('SELECT COUNT(*) c FROM threats').fetchone()['c']; active=con.execute("SELECT COUNT(*) c FROM threats WHERE status NOT IN ('CLOSED','FALSE_POSITIVE')").fetchone()['c']; critical=con.execute("SELECT COUNT(*) c FROM threats WHERE severity='CRITICAL'").fetchone()['c']; high=con.execute("SELECT COUNT(*) c FROM threats WHERE severity='HIGH'").fetchone()['c']; inv=con.execute("SELECT COUNT(*) c FROM threats WHERE status='UNDER_REVIEW'").fetchone()['c']; avg=con.execute('SELECT AVG(confidence_score) x FROM threats').fetchone()['x'] or 0; vuln=con.execute("SELECT COUNT(*) c FROM threats WHERE cve_id!=''").fetchone()['c']; alerts=con.execute("SELECT COUNT(*) c FROM alerts WHERE status NOT IN ('RESOLVED','FALSE_POSITIVE')").fetchone()['c']; con.close(); return {'total_threat_records':total,'critical_threats':critical,'high_threats':high,'active_indicators':active,'open_investigations':inv,'average_confidence':round(avg,1),'vulnerabilities_tracked':vuln,'active_alerts':alerts}
@app.get('/api/dashboard/trends')
def trends():
    con=db(); rows=con.execute("SELECT substr(first_seen,1,10) day,COUNT(*) count FROM threats GROUP BY day ORDER BY day").fetchall(); sev=con.execute('SELECT severity,COUNT(*) count FROM threats GROUP BY severity').fetchall(); cat=con.execute('SELECT category,COUNT(*) count FROM threats GROUP BY category ORDER BY count DESC').fetchall(); types=con.execute('SELECT indicator_type,COUNT(*) count FROM threats GROUP BY indicator_type').fetchall(); tactics=con.execute("SELECT mitre_tactic,COUNT(*) count FROM threats WHERE mitre_tactic!='' GROUP BY mitre_tactic ORDER BY count DESC").fetchall(); risks=con.execute("SELECT CASE WHEN risk_score<=20 THEN 'INFORMATIONAL' WHEN risk_score<=40 THEN 'LOW' WHEN risk_score<=60 THEN 'MEDIUM' WHEN risk_score<=80 THEN 'HIGH' ELSE 'CRITICAL' END bucket,COUNT(*) count FROM threats GROUP BY bucket").fetchall(); conf=con.execute("SELECT CASE WHEN confidence_score<=40 THEN 'LOW' WHEN confidence_score<=70 THEN 'MEDIUM' ELSE 'HIGH' END bucket,COUNT(*) count FROM threats GROUP BY bucket").fetchall(); status=con.execute('SELECT status,COUNT(*) count FROM threats GROUP BY status').fetchall(); con.close(); return {'over_time':[dict(r) for r in rows],'severity':[dict(r) for r in sev],'category':[dict(r) for r in cat],'indicator_types':[dict(r) for r in types],'tactics':[dict(r) for r in tactics],'risk_distribution':[dict(r) for r in risks],'confidence_distribution':[dict(r) for r in conf],'status':[dict(r) for r in status]}
@app.get('/api/threats')
def threats(severity:Optional[str]=None,category:Optional[str]=None,indicator_type:Optional[str]=None,status:Optional[str]=None,min_risk:int=0,max_risk:int=100,min_confidence:int=0,max_confidence:int=100,sort:str='newest',limit:int=100):
    sql='SELECT * FROM threats WHERE risk_score BETWEEN ? AND ? AND confidence_score BETWEEN ? AND ?'; args=[min_risk,max_risk,min_confidence,max_confidence]
    for col,val in [('severity',severity),('category',category),('indicator_type',indicator_type),('status',status)]:
        if val: sql+=f' AND {col}=?'; args.append(val)
    sql+=' ORDER BY '+({'highest_risk':'risk_score DESC','highest_confidence':'confidence_score DESC','most_observed':'observation_count DESC','newest':'last_seen DESC'}.get(sort,'last_seen DESC'))+' LIMIT ?'; args.append(min(limit,500)); con=db(); rows=con.execute(sql,args).fetchall(); con.close(); return [dict(r) for r in rows]
@app.get('/api/threats/{threat_id}')
def threat(threat_id:str):
    con=db(); r=con.execute('SELECT * FROM threats WHERE threat_id=?',(threat_id,)).fetchone(); notes=con.execute('SELECT * FROM analyst_notes WHERE threat_id=? ORDER BY created_at DESC',(threat_id,)).fetchall(); related=[]
    if r: related=con.execute('SELECT threat_id,indicator_type,indicator_value,category,risk_score FROM threats WHERE campaign_id=? AND threat_id!=? LIMIT 20',(r['campaign_id'],threat_id)).fetchall()
    con.close();
    if not r: raise HTTPException(404,'Threat not found')
    d=dict(r); d['analyst_notes']=[dict(x) for x in notes]; d['related_indicators']=[dict(x) for x in related]; d['recommended_actions']=['Review authorized internal telemetry','Check related synthetic observations','Review email/security controls','Increase awareness for the relevant category','Monitor related indicators']; return d
@app.post('/api/threats')
def create_threat(x:ThreatCreate):
    v=validate_indicator(x.indicator_value,x.indicator_type)
    if not v['valid']: raise HTTPException(422,v['validation_notes'])
    tid=f'THR-CUSTOM-{datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")[:17]}'; now=datetime.now(timezone.utc).isoformat(); con=db(); con.execute('INSERT INTO threats VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(tid,x.threat_name,x.category,x.description,x.severity,x.risk_score,x.confidence_score,x.status,now,now,v['indicator_type'],v['normalized_value'],x.source_name,'C','', '', '', 'CUSTOM',1)); con.commit(); con.close(); return {'threat_id':tid}
@app.get('/api/indicators/search')
def indicator_search(q:str=Query(min_length=1,max_length=500)):
    v=validate_indicator(q); rows=load_records(); e=enrich_indicator(v['normalized_value'],rows) if v['valid'] else {'known_in_demo_dataset':False}; con=db(); matches=con.execute('SELECT threat_id,threat_name,category,indicator_type,indicator_value,severity,risk_score,confidence_score,first_seen,last_seen,status FROM threats WHERE lower(indicator_value)=lower(?) LIMIT 50',(v['normalized_value'],)).fetchall(); con.close(); return {'validation':v,'enrichment':e,'matches':[dict(r) for r in matches]}
@app.get('/api/alerts')
def alerts(status:Optional[str]=None):
    con=db(); sql='SELECT * FROM alerts'; args=[]
    if status: sql+=' WHERE status=?'; args.append(status)
    rows=con.execute(sql+' ORDER BY timestamp DESC LIMIT 200',args).fetchall(); con.close(); return [dict(r) for r in rows]
@app.put('/api/alerts/{alert_id}/status')
def update_alert(alert_id:str,x:AlertStatus,_auth=__import__('fastapi').Depends(analyst_auth)):
    if x.status not in {'NEW','INVESTIGATING','MONITORING','RESOLVED','FALSE_POSITIVE'}: raise HTTPException(422,'Invalid alert status')
    con=db(); r=con.execute('SELECT status FROM alerts WHERE alert_id=?',(alert_id,)).fetchone();
    if not r: con.close(); raise HTTPException(404,'Alert not found')
    con.execute('UPDATE alerts SET status=? WHERE alert_id=?',(x.status,alert_id)); con.execute('INSERT INTO audit_log(action,target_id,old_value,new_value,created_at) VALUES(?,?,?,?,?)',('ALERT_STATUS_UPDATE',alert_id,r['status'],x.status,datetime.now(timezone.utc).isoformat())); con.commit(); con.close(); return {'alert_id':alert_id,'status':x.status}
@app.post('/api/threats/{threat_id}/notes')
def add_note(threat_id:str,x:NoteCreate,_auth=__import__('fastapi').Depends(analyst_auth)):
    con=db();
    if not con.execute('SELECT 1 FROM threats WHERE threat_id=?',(threat_id,)).fetchone(): con.close(); raise HTTPException(404,'Threat not found')
    now=datetime.now(timezone.utc).isoformat(); con.execute('INSERT INTO analyst_notes(threat_id,note,created_at) VALUES(?,?,?)',(threat_id,x.note,now)); con.commit(); con.close(); return {'threat_id':threat_id,'created_at':now}
@app.get('/api/vulnerabilities')
def vulnerabilities():
    with (DATA/'vulnerabilities.csv').open(encoding='utf-8') as f: rows=list(csv.DictReader(f))
    for r in rows:r['priority_score']=calculate_vulnerability_priority(float(r['cvss_score']),float(r['asset_criticality']),float(r['exposure']),float(r['known_exploitation']),float(r['business_context']))
    return rows
@app.get('/api/awareness/modules')
def modules(): return json.loads((AWARE/'modules.json').read_text(encoding='utf-8'))
@app.get('/api/quiz')
def quiz():
    q=json.loads((AWARE/'quiz_questions.json').read_text(encoding='utf-8')); return [{k:v for k,v in x.items() if k!='answer'} for x in q]
@app.post('/api/quiz/submit')
def quiz_submit(x:QuizSubmit):
    q=json.loads((AWARE/'quiz_questions.json').read_text(encoding='utf-8')); by={str(a['id']):a for a in q}; scores={}; correct=0
    for k,a in x.answers.items():
        if k in by:
            cat=by[k]['category']; scores.setdefault(cat,[0,0]); scores[cat][1]+=1; correct+=a==by[k]['answer']; scores[cat][0]+=a==by[k]['answer']
    total=len(x.answers); overall=round(correct/total*100) if total else 0
    label='Needs Improvement' if overall<=40 else 'Basic Awareness' if overall<=60 else 'Good Awareness' if overall<=80 else 'Strong Awareness'
    category_scores={k:round(v[0]/v[1]*100) for k,v in scores.items()}; weak=[k for k,v in category_scores.items() if v<61]
    return {'overall_score':overall,'level':label,'category_scores':category_scores,'weakest_areas':weak,'recommendations':[f'Review the {c} module' for c in weak],'correct':correct,'total':total}
@app.get('/api/executive/summary')
def executive():
    s=stats(); con=db(); cats=con.execute('SELECT category,COUNT(*) count FROM threats GROUP BY category ORDER BY count DESC LIMIT 5').fetchall(); vul=con.execute("SELECT category,COUNT(*) count FROM threats WHERE cve_id!='' GROUP BY category ORDER BY count DESC").fetchall(); con.close(); return {'kpis':s,'top_categories':[dict(x) for x in cats],'vulnerability_categories':[dict(x) for x in vul],'awareness_score_trend':[58,62,67,71,76,79],'top_awareness_weaknesses':['Phishing','Social Engineering','Incident Reporting'],'recommended_priorities':['Review critical/high synthetic threats','Prioritize contextually important vulnerabilities','Run phishing and social-engineering awareness modules']}
@app.get('/api/attack')
def attack():
    con=db(); rows=con.execute("SELECT mitre_tactic tactic,mitre_technique technique,COUNT(*) count FROM threats WHERE mitre_tactic!='' GROUP BY tactic,technique ORDER BY count DESC").fetchall(); con.close(); return [dict(x) for x in rows]
