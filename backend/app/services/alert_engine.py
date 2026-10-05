def generate_threat_alert(r):
    if r['risk_score']>=75 or (r['confidence_score']>=85 and r['risk_score']>=60):
        return {'alert_id':f"ALT-{r['threat_id'].replace('THR-','')}",'threat_id':r['threat_id'],'timestamp':r['last_seen'],'alert_type':'HIGH_RISK_INDICATOR','severity':r['severity'],'risk_score':r['risk_score'],'confidence_score':r['confidence_score'],'description':f"Synthetic intelligence record {r['threat_id']} warrants analyst review.",'status':'NEW'}
    return None
def correlate_alerts(observations):
    groups={}
    for o in observations:
        k=o.get('indicator_value','unknown'); groups.setdefault(k,[]).append(o)
    return [{'indicator_value':k,'observation_count':len(v),'correlated_alert_count':1,'status':'CORRELATED'} for k,v in groups.items()]
