from datetime import datetime,timezone
SEV={'INFORMATIONAL':10,'LOW':30,'MEDIUM':50,'HIGH':70,'CRITICAL':95}
SOURCE={'A':95,'B':80,'C':65,'D':35}
def classify_score(score:int)->str:
    score=max(0,min(100,int(round(score))))
    return 'INFORMATIONAL' if score<=20 else 'LOW' if score<=40 else 'MEDIUM' if score<=60 else 'HIGH' if score<=80 else 'CRITICAL'
def calculate_threat_risk(severity,confidence,recency,observation_frequency,source_reliability,context_correlation):
    score=.30*SEV.get(str(severity).upper(),50)+.25*confidence+.15*recency+.10*observation_frequency+.10*SOURCE.get(str(source_reliability).upper(),50)+.10*context_correlation
    return max(0,min(100,round(score)))
def recency_score(last_seen):
    try:
        dt=datetime.fromisoformat(last_seen.replace('Z','+00:00')); days=max(0,(datetime.now(timezone.utc)-dt).days); return max(0,100-min(100,days*5))
    except Exception:return 50
def calculate_vulnerability_priority(cvss,asset_criticality,exposure,known_exploitation,business_context):
    score=.35*(cvss*10)+.20*asset_criticality+.15*exposure+.20*known_exploitation+.10*business_context
    return round(max(0,min(100,score)))
