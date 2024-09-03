from scraper import get_game_result, get_news_title, search_api
from sms import *
import re
import time

WORDS = ["سلام", "شروع", "استارت", "start", "آغاز", "راهنما", "نتیجه"]
guide = "سلام , به فوتبالیار خوش امدید \n برای دریافت نتایج تیم های مورد نظر تون رو به صورت تیم۱!تیم۲ ارسال کنید\n برای دریافت اخبار روز کلمه اخبار و برای جستجو در خبر ها عبارت مد نظر خودتون برای جستجو رو به صورت اخبار:عبارت شما ارسال نمایید.\n با تشکر از همراهی شما"


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

            elif msg == "اخبار":
                sendMessange(get_news_title(), sender)
                return get_news_title()

            elif "اخبار:" in msg:
                sendMessange(search_api(msg), sender)
                return search_api(msg)


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
