import os
from kavenegar import *

api = KavenegarAPI(os.environ.get("kavenegar_key"))


def sendMessange(msg, receptor):
    global api
    try:
        params = {'sender': '200090908000', 'receptor': receptor, 'message': msg}
        api.sms_send(params)
    except:
        print("you have a problem in sending message")


def getinbox():
    global api
    params = {'linenumber': '200090908000', 'isread': 0}
    response = api.sms_receive(params)
    if len(response) > 0:
        for msg in response:
            result = msg['message']
            sender = msg['sender']
            return [result, sender]
