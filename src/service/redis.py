import requests
import json 

def get_redis_OTP(user_id: int):
    hash= "otp" + user_id
    url = "rdis api hecha por jcamilofarfan/" + hash
    headers= {
        'X-Type-Value': 'value'
    }
    res = requests.get(url, headers=headers)
    response = json.loads(res.text)
    return response

