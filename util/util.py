import time
import hmac
import base64
import os
from datetime import datetime , timezone , timedelta
def get_difference_bp(old,new):
    return round((new-old)/old*10000,3)

def time_now():
    now = datetime.utcnow( ) +timedelta(hours=8)
    return now.strftime('%Y/%m/%d %H:%M:%S.%f')

def kill_program():
    print("Killing the program")
    os._exit(0)

def timestamp_now():
    return datetime.timestamp(datetime.utcnow())

def millisecond_to_datetime(millisecond:int)->str:
    second = millisecond/1000
    return datetime.fromtimestamp(second,tz=timezone.utc).isoformat()
def get_local_timestamp():
    return int(time.time())
def okx_login_params(api_key, api_secret_key, passphrase):
    ts = get_local_timestamp()
    message = str(ts) + 'GET' + '/users/self/verify'

    mac = hmac.new(bytes(api_secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    sign = base64.b64encode(d)

    login_param = {"op": "login", "args": [{"apiKey": api_key,
                                            "passphrase": passphrase,
                                            "timestamp": ts,
                                            "sign": sign.decode("utf-8")}]}

    return login_param