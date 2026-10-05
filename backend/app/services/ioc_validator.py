import ipaddress,re
from urllib.parse import urlparse
DOMAIN_RE=re.compile(r'^(?=.{1,253}$)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}$')
CVE_RE=re.compile(r'^CVE-\d{4}-\d{4,}$',re.I)
HASHES={'MD5':re.compile(r'^[0-9a-fA-F]{32}$'),'SHA1':re.compile(r'^[0-9a-fA-F]{40}$'),'SHA256':re.compile(r'^[0-9a-fA-F]{64}$')}
def validate_indicator(value:str, indicator_type:str|None=None):
    value=(value or '').strip()
    if not value:return {'valid':False,'indicator_type':indicator_type or 'UNKNOWN','normalized_value':'','validation_notes':'Indicator is required.'}
    checks=[]
    try:
        ip=ipaddress.ip_address(value); checks.append(('IP ADDRESS',str(ip)))
    except ValueError: pass
    if DOMAIN_RE.fullmatch(value.lower()): checks.append(('DOMAIN',value.lower().rstrip('.')))
    try:
        p=urlparse(value)
        if p.scheme.lower() in ('http','https') and p.hostname: checks.append(('URL',value))
    except ValueError: pass
    for name,rx in HASHES.items():
        if rx.fullmatch(value): checks.append(('FILE HASH',value.lower()))
    if CVE_RE.fullmatch(value): checks.append(('CVE ID',value.upper()))
    if indicator_type:
        wanted=indicator_type.upper()
        for t,v in checks:
            if wanted in (t, 'HASH' if t=='FILE HASH' else t): return {'valid':True,'indicator_type':t,'normalized_value':v,'validation_notes':'Syntactically valid; validity does not establish maliciousness.'}
        return {'valid':False,'indicator_type':wanted,'normalized_value':value,'validation_notes':'Value does not match the requested indicator format.'}
    if checks:
        t,v=checks[0]; return {'valid':True,'indicator_type':t,'normalized_value':v,'validation_notes':'Syntactically valid; validity does not establish maliciousness.'}
    return {'valid':False,'indicator_type':'UNKNOWN','normalized_value':value,'validation_notes':'Unsupported or invalid indicator format.'}
