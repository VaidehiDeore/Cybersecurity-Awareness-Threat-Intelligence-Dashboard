import os
from fastapi import Header,HTTPException

def analyst_auth(x_analyst_key:str|None=Header(default=None)):
    expected=os.getenv('ANALYST_API_KEY','demo-analyst-key')
    if os.getenv('APP_ENV','development')=='production' and x_analyst_key!=expected:
        raise HTTPException(status_code=401,detail='Analyst authentication required')
    return True
