def enrich_indicator(indicator,records):
    hits=[r for r in records if str(r.get('indicator_value','')).lower()==indicator.lower()]
    if not hits:return {'known_in_demo_dataset':False,'indicator_type':None,'related_alerts':[],'related_indicators':[]}
    rank={'INFORMATIONAL':1,'LOW':2,'MEDIUM':3,'HIGH':4,'CRITICAL':5}
    best=max(hits,key=lambda x:rank.get(str(x.get('severity','MEDIUM')).upper(),3))
    mappings=[]
    for r in hits:
        tech=r.get('mitre_technique_optional','')
        if tech:mappings.append((r.get('mitre_tactic_optional',''),tech))
    return {'known_in_demo_dataset':True,'indicator_type':hits[0].get('indicator_type'),'first_seen':min(r.get('first_seen','') for r in hits),'last_seen':max(r.get('last_seen','') for r in hits),'categories':sorted(set(r.get('threat_category','') for r in hits)),'confidence':round(sum(int(r.get('confidence_score',0)) for r in hits)/len(hits)),'severity':best.get('severity'),'risk':max(int(r.get('risk_score',0)) for r in hits),'related_alerts':[],'related_indicators':sorted(set(str(r.get('indicator_value')) for r in hits if str(r.get('indicator_value','')).lower()!=indicator.lower())),'mitre_mapping':sorted(set(mappings))}
