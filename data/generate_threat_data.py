from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import csv,random,hashlib
from datetime import datetime,timedelta,timezone
from backend.app.services.risk_engine import calculate_threat_risk,classify_score
from backend.app.services.attack_mapper import map_attack
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'data/threat_intelligence_dataset.csv'; random.seed(42)
cats=['PHISHING','MALWARE','RANSOMWARE','CREDENTIAL THEFT','WEB THREATS','NETWORK THREATS','VULNERABILITY EXPLOITATION AWARENESS','SOCIAL ENGINEERING','DATA EXPOSURE','ACCOUNT TAKEOVER RISK']
types=['IP ADDRESS','DOMAIN','URL','FILE HASH','EMAIL/SENDER DOMAIN']
sources=[('Internal SOC','A'),('Security Vendor','A'),('Public Threat Feed','B'),('Research Report','B'),('Community Submission','C'),('Unknown Source','D')]
sevs=['INFORMATIONAL','LOW','MEDIUM','HIGH','CRITICAL']; statuses=['NEW','UNDER_REVIEW','MONITORING','CLOSED','FALSE_POSITIVE']
fields=['threat_id','timestamp','threat_name','threat_category','indicator_type','indicator_value','source_name','confidence_score','severity','risk_score','status','first_seen','last_seen','country_or_region_optional','description','mitre_tactic_optional','mitre_technique_optional','cve_id_optional','campaign_id','observation_count','source_reliability']
base=datetime.now(timezone.utc)-timedelta(days=90)
def indicator(t,i):
    n=i%6
    if t=='IP ADDRESS': return ['192.0.2.25','198.51.100.25','203.0.113.42','192.0.2.77','198.51.100.90'][n%5]
    if t=='DOMAIN': return ['login-check.invalid','security-update.example.com','account-review.example.org','mail-alert.example.net','verify-user.invalid'][n%5]
    if t=='URL': return ['https://login-check.invalid/verify','https://security-update.example.com/notice','https://account-review.example.org/login','https://mail-alert.example.net/update'][n%4]
    if t=='FILE HASH': return hashlib.sha256(f'synthetic-{i}'.encode()).hexdigest()
    return ['example.com','example.org','example.net','invalid'][n%4]
rows=[]
for i in range(1,2001):
    cat=random.choice(cats); typ=random.choice(types); src,rel=random.choice(sources); first=base+timedelta(days=random.randint(0,85),hours=random.randint(0,23)); last=first+timedelta(hours=random.randint(1,240)); conf=random.randint(35,98); sev=random.choices(sevs,weights=[5,15,30,35,15])[0]; rec=max(0,100-(datetime.now(timezone.utc)-last).days*5); freq=random.randint(10,100); context=random.randint(10,100); risk=calculate_threat_risk(sev,conf,rec,freq,rel,context); cat2,tech,tid=map_attack(cat); cve=f'CVE-2099-{10000+i}' if 'VULNERABILITY' in cat else ''
    rows.append({'threat_id':f'THR-2026-{i:04d}','timestamp':last.isoformat(),'threat_name':('Synthetic '+cat.title()+' Observation'),'threat_category':cat,'indicator_type':typ,'indicator_value':indicator(typ,i),'source_name':src,'confidence_score':conf,'severity':classify_score(risk),'risk_score':risk,'status':random.choice(statuses),'first_seen':first.isoformat(),'last_seen':last.isoformat(),'country_or_region_optional':random.choice(['APAC','North America','Europe','Global','Synthetic Region']),'description':f'SYNTHETIC / DEMO ONLY. Defensive intelligence record for {cat.lower()}. No malicious activity is executed or contacted.','mitre_tactic_optional':cat2 or '','mitre_technique_optional':f'{tech} ({tid})' if tech else '','cve_id_optional':cve,'campaign_id':f'CAMP-{(i%80)+1:03d}','observation_count':random.randint(1,25),'source_reliability':rel})
with OUT.open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
print(f'Generated {len(rows)} synthetic records at {OUT}')
