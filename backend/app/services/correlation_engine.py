from collections import defaultdict
def correlate_threats(records):
    groups=defaultdict(list)
    for r in records:
        key=r.get('campaign_id') or f"{r['threat_category']}|{r['first_seen'][:10]}"
        groups[key].append(r)
    clusters=[]
    for key,items in groups.items():
        if len(items)>1: clusters.append({'cluster_id':f'CL-{len(clusters)+1:03d}','basis':'shared campaign/observation context','records':[r['threat_id'] for r in items],'indicator_count':len(items),'note':'Correlation indicates relationship/evidence, not guaranteed attribution.'})
    return clusters
def correlate_alerts(observations):
    groups=defaultdict(list)
    for o in observations: groups[o.get('indicator_value','unknown')].append(o)
    out=[]
    for indicator,items in groups.items():
        out.append({'indicator_value':indicator,'observation_count':len(items),'correlated':len(items)>1,'alert_count':1,'note':'Repeated observations are consolidated to reduce alert fatigue.'})
    return out
