from kavenegar import *

api = KavenegarAPI('6C6743424E626D6F774D5A3534614D687456413561334B2B6362634C4E476E366A3066516A6261746F2B6B3D')


def sendMessange(result, receptor):
    global api
    try:
        params = {'receptor': receptor, 'message': result}
        api.sms_send(params)
    except:
        print("you have a problem in sending message")


def getinbox():
    global api
    params = {'linenumber': '200090908000', 'isread': 0}
    response = api.sms_receive(params)

    if response['entries']:
        for entry in response['entries']:
            result = entry['message']
            return [result, receptor]

    print("you have an error while getting message")
