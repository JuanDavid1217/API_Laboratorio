import random
from datetime import datetime

######    TOKENS    ######

def generate_token(tokens: list[str]):
    token = ''
    while True:
        token = create_token()
        if token not in tokens:
            break
    return token 
        
def create_token():
    data="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    token=""
    for i in range(6):
        token += random.choice(data)
    return token
    
def token_validation(start_date:str):
    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - start_date).total_seconds() <= 300:
        return True
    else:
    	return False
    
######    DATES    ######

def date_validation(date:str):
    try:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return True
    except Exception as e:
        return False
    
    
#print(generate_token(['iExahW', 'dilMgg', 'q9XdAC']))
#print(token_validation('2024-10-04 23:35:00'))
#print(date_validation('2023-02-29 23:35:00'))
