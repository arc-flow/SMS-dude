from scraper import get_game_result
from sms import *
import re
import time

WORDS = ["سلام", "شروع", "استارت", "start", "آغاز", "راهنما", "نتیجه"]
guide = ""


def main():
    msg, receptor = getinbox()
    if msg in WORDS:
        sendMessange(guide, receptor)
        return guide
    else:
        if re.match("^.+[,!:].+$", msg):
            team1, team2 = re.split(",!:", msg)
            team1 = re.sub(" +", " ", team1)
            team2 = re.sub(" +", " ", team2)
            result = get_game_result(team1, team2)
            sendMessange(result, receptor)


while True:
    main()
    time.sleep(0.5)
