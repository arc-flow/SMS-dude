from kavenegar import *

api = KavenegarAPI('6C6743424E626D6F774D5A3534614D687456413561334B2B6362634C4E476E366A3066516A6261746F2B6B3D')


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
    print(response)
    if len(response) > 0:
        for msg in response:
            result = msg['message']
            sender = msg['sender']
            return [result, sender]

    print("you have an error while getting message")
