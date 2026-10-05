ATTACK_MAP={
'PHISHING':('Initial Access','Phishing','T1566'),
'MALWARE':('Execution','Command and Scripting Interpreter','T1059'),
'RANSOMWARE':('Impact','Data Encrypted for Impact','T1486'),
'CREDENTIAL THEFT':('Credential Access','Valid Accounts','T1078'),
'SOCIAL ENGINEERING':('Initial Access','Phishing','T1566'),
'ACCOUNT TAKEOVER RISK':('Credential Access','Valid Accounts','T1078')}
def map_attack(category,context=''):
    if category.upper() in ATTACK_MAP:return ATTACK_MAP[category.upper()]
    return (None,None,None)
