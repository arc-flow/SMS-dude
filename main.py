from scraper import *
from sms import *
import re
import time

WORDS = ["سلام", "شروع", "استارت", "start", "آغاز", "راهنما", "نتیجه"]
guide = "سلام؛\nلیست دستور های فوتبالیار:\nمشاهده نتیجه یک بازی : نام تیم!نام تیم\nمشاهده لیگ های امروز : امروز\nمشاهده بازی های یک لیگ : امروز:شماره لیگ\n«دستور های دیروز و فردا هم به همین صورت هستند.»\nمشاهده اخبار برتر : اخبار\nمشاهده اخبار یک تیم : اخبار:نام تیم\n\nدستور های چت جی پی تی:\nشروع چت : چت\nپیام به چت جی پی تی : چت:محتوای پیام\nکاری از تیم «ArcFlow»"
customers = []


def main():
    inbox = getinbox()
    if inbox is not None:
        if len(inbox) > 0:
            msg, sender = inbox
            print(f"{sender} -> {msg}")
            if msg in WORDS:
                if sender not in customers:
                    sendMessange(guide, sender)
                    customers.append(sender)
                    return guide

            elif msg == "اخبار":
                sendMessange(get_news_title(), sender)

            elif msg.startswith("اخبار:"):
                sendMessange(search_api(msg), sender)
            elif msg == "چت":
                sendMessange(gpt_hi(), sender)
            elif msg.startswith("چت:"):
                sendMessange(gpt_API(msg), sender)

            elif msg == "امروز":
                sendMessange("لیگ خود را به صورت امروز:شماره لیگ انتخاب کنید." + "\n" + get_leagues(0), sender)
            elif msg.startswith("امروز:"):
                sendMessange(get_games(msg, 0), sender)
            elif msg == "دیروز":
                sendMessange("لیگ خود را به صورت دیروز:شماره لیگ انتخاب کنید." + "\n" + get_leagues(-1), sender)
            elif msg.startswith("دیروز:"):
                sendMessange(get_games(msg, -1), sender)
            elif msg == "فردا":
                sendMessange("لیگ خود را به صورت فردا:شماره لیگ انتخاب کنید." + "\n" + get_leagues(1), sender)
            elif msg.startswith("فردا:"):
                sendMessange(get_games(msg, 1), sender)
            else:
                if re.match("^.+[!].+$", msg):
                    team1, team2 = msg.split("!")
                    team1 = re.sub(" +", " ", team1)
                    team2 = re.sub(" +", " ", team2)
                    result = get_game_result(team1, team2)
                    sendMessange(result, sender)


while True:
    try:
        main()
    except Exception as e:
        print(e)
    time.sleep(3)
