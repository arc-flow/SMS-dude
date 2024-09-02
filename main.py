from scraper import get_game_result
from sms import *
import re
import time

WORDS = ["سلام", "شروع", "استارت", "start", "آغاز", "راهنما", "نتیجه"]
guide = "برای دریافت نتایج تیم های مورد نظر تون رو به صورت تیم۱!تیم۲ ارسال کنید"


def main():
    inbox = getinbox()
    if inbox is not None:
        if len(inbox) > 0:
            msg, sender = inbox
            print(msg)
            print(sender)
            if msg in WORDS:
                sendMessange(guide, sender)
                print("guide")
                return guide
            else:
                if re.match("^.+[!].+$", msg):
                    team1, team2 = msg.split("!")
                    team1 = re.sub(" +", " ", team1)
                    team2 = re.sub(" +", " ", team2)
                    result = get_game_result(team1, team2)
                    sendMessange(result, sender)
                    print(result)
                    return result
    else:
        print("no message")
        return "no message"


while True:
    try:
        main()
    except Exception as e:
        print(e)
    time.sleep(3)
