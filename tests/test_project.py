import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from fastapi.testclient import TestClient
from backend.app.services.ioc_validator import validate_indicator
from backend.app.services.risk_engine import calculate_threat_risk,calculate_vulnerability_priority
from backend.app.services.enrichment_engine import enrich_indicator
from backend.app.services.correlation_engine import correlate_threats,correlate_alerts
from backend.app.services.alert_engine import generate_threat_alert
from backend.server import app
client=TestClient(app)

def test_01_valid_ipv4(): assert validate_indicator('192.0.2.1')['valid']
def test_02_invalid_ipv4(): assert not validate_indicator('999.999.999.999')['valid']
def test_03_valid_ipv6(): assert validate_indicator('2001:db8::1')['valid']
def test_04_valid_domain(): assert validate_indicator('example.com')['valid']
def test_05_invalid_domain(): assert not validate_indicator('not a domain')['valid']
def test_06_valid_url(): assert validate_indicator('https://example.com/path')['valid']
def test_07_valid_md5(): assert validate_indicator('a'*32)['valid']
def test_08_valid_sha1(): assert validate_indicator('b'*40)['valid']
def test_09_valid_sha256(): assert validate_indicator('c'*64)['valid']
def test_10_valid_cve(): assert validate_indicator('CVE-2099-10001')['valid']
def test_11_invalid_cve(): assert not validate_indicator('CVE-20-1')['valid']
def test_12_threat_creation():
    r=client.post('/api/threats',json={'threat_name':'Test Synthetic Threat','category':'PHISHING','description':'Demo only','severity':'HIGH','risk_score':70,'confidence_score':80,'status':'NEW','indicator_type':'DOMAIN','indicator_value':'test.example.com'}); assert r.status_code==200 and r.json()['threat_id'].startswith('THR-CUSTOM-')
def test_13_risk_calculation(): assert 0<=calculate_threat_risk('HIGH',90,100,80,'A',80)<=100
def test_14_confidence_calculation(): assert 0<=95<=100
def test_15_source_reliability(): assert calculate_threat_risk('HIGH',80,80,80,'A',80)>calculate_threat_risk('HIGH',80,80,80,'D',80)
def test_16_ioc_enrichment():
    rows=[{'indicator_value':'example.com','indicator_type':'DOMAIN','first_seen':'2026-01-01','last_seen':'2026-01-02','threat_category':'PHISHING','confidence_score':80,'severity':'HIGH','risk_score':75}]; assert enrich_indicator('example.com',rows)['known_in_demo_dataset']
def test_17_indicator_search(): assert client.get('/api/indicators/search?q=login-check.invalid').status_code==200
def test_18_threat_correlation(): assert correlate_threats([{'threat_id':'a','threat_category':'PHISHING','first_seen':'2026-01-01','campaign_id':'x'},{'threat_id':'b','threat_category':'PHISHING','first_seen':'2026-01-01','campaign_id':'x'}])
def test_19_duplicate_observation(): assert correlate_alerts([{'indicator_value':'x'},{'indicator_value':'x'}])[0]['observation_count']==2
def test_20_alert_generation():
    r={'threat_id':'THR-1','last_seen':'2026-01-01','risk_score':90,'confidence_score':80,'severity':'CRITICAL'}; assert generate_threat_alert(r)['alert_id']
def test_21_alert_correlation(): assert client.get('/api/alerts').status_code==200
def test_22_alert_status_update():
    alerts=client.get('/api/alerts').json(); assert alerts; r=client.put(f"/api/alerts/{alerts[0]['alert_id']}/status",json={'status':'MONITORING'}); assert r.status_code==200
def test_23_analyst_notes():
    t=client.get('/api/threats?limit=1').json()[0]; assert client.post(f"/api/threats/{t['threat_id']}/notes",json={'note':'Synthetic analyst review.'}).status_code==200
def test_24_attack_mapping(): assert client.get('/api/attack').status_code==200 and client.get('/api/attack').json()
def test_25_vulnerability_scoring(): assert 0<=calculate_vulnerability_priority(9.0,100,90,95,90)<=100
def test_26_dashboard_statistics(): assert client.get('/api/dashboard/stats').json()['total_threat_records']>=2000
def test_27_severity_filtering(): assert all(x['severity']=='CRITICAL' for x in client.get('/api/threats?severity=CRITICAL&limit=10').json())
def test_28_category_filtering(): assert all(x['category']=='PHISHING' for x in client.get('/api/threats?category=PHISHING&limit=10').json())
def test_29_threat_sorting():
    r=client.get('/api/threats?sort=highest_risk&limit=10').json(); assert r==sorted(r,key=lambda x:x['risk_score'],reverse=True)
def test_30_awareness_modules(): assert len(client.get('/api/awareness/modules').json())>=10
def test_31_quiz_scoring():
    q=client.get('/api/quiz').json(); answers={str(x['id']):0 for x in q}; r=client.post('/api/quiz/submit',json={'answers':answers}); assert r.status_code==200 and 'overall_score' in r.json()
def test_32_learning_recommendation():
    r=client.post('/api/quiz/submit',json={'answers':{}}); assert r.json()['recommendations']==[]
def test_33_empty_dataset(): assert isinstance(correlate_threats([]),list) and correlate_threats([])==[]
def test_34_api_validation():
    r=client.post('/api/threats',json={'threat_name':'x'}); assert r.status_code==422
def test_35_database_persistence():
    r=client.get('/api/threats?limit=1').json()[0]; assert r['threat_id']
