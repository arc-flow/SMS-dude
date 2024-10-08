import requests
import os
from unidecode import unidecode
from langchain_openai import ChatOpenAI


def get_matches_data():
    data = []
    for day in range(-2, 1):
        API_URL_MATCHES = f"https://web-api.varzesh3.com/v1.0/livescore/{day}"
        r = requests.get(API_URL_MATCHES)
        if r.status_code == 200:
            data += r.json()["matches"]
    return data


def calculate_result(match):
    goals = []
    events = requests.get(match["eventsApi"])
    for event in events.json():
        if "goalType" in event:
            goals.append(event["description"])
    match_result = f'{match["hostName"]} {match["matchGoals"]["host"]} - {match["matchGoals"]["guest"]} {match["guestName"]}'
    for goal in goals:
        match_result += f'\n{goal}'
    return match_result


def get_game_result(team1, team2):
    data = get_matches_data()
    for match in data:
        if match["hostName"] == team1 and match["guestName"] == team2:
            return calculate_result(match)
        elif match["hostName"] == team2 and match["guestName"] == team1:
            return calculate_result(match)


def get_news_title():
    data = []
    titles = []
    API_URL_NEWS = "https://web-api.varzesh3.com/v1.0/news/most-commented?includeSports[0]=Football&includeSports[1]=Futsal&includeSports[2]=BeachSoccer"
    request = requests.get(API_URL_NEWS)
    data += request.json()
    if request.status_code == 200:
        for object in data:
            titles.append(object["title"])
    return f"{titles[0]}\n{titles[1]}\n{titles[2]}\n{titles[3]}\n{titles[4]}"


def search_api(result):
    data = []
    titles = []
    word = result.split(":")
    API_URL = f"https://search-api.varzesh3.com/v1.0/query?q={word[1]}"
    request = requests.get(API_URL)
    data += request.json()['news']
    if request.status_code == 200:
        for object in data:
            titles.append(object["title"])
    return f"{titles[0]}\n{titles[1]}\n{titles[2]}\n{titles[3]}\n{titles[4]}"
openai_api_key=os.environ.get("openai_api_key")
llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        base_url="https://api.avalai.ir/v1",
        api_key=openai_api_key)

def gpt_API(message):
    thingtosend = message.split(":")
    global llm
    return llm.invoke(thingtosend[1] + "--very_short, very_short, --summarized, summarized").content


def gpt_hi():
    global llm
    return llm.invoke("سلام؟!").content


def get_leagues(day):
    leagues = ""
    API_URL = f"https://web-api.varzesh3.com/v1.0/livescore/{day}"
    r = requests.get(API_URL)
    if r.status_code == 200:
        r = r.json()
        for i, league in enumerate(r["leagues"], 1):
            leagues += f'{i}-{league["title"]}\n'
        return leagues


def get_games(msg, day):
    matches = ""
    league_id = int(unidecode(msg.split(":")[-1]))
    API_URL = f"https://web-api.varzesh3.com/v1.0/livescore/{day}"
    r = requests.get(API_URL)
    if r.status_code == 200:
        r = r.json()
        all_matches = r["matches"]
        current_league = r["leagues"][league_id - 1]
        for matchId in current_league["dates"][0]["matchIds"]:
            for match in all_matches:
                if match["sportId"] == matchId:
                    matches += f'{match["scheduledStartTime"]} {match["hostName"]} {match["matchGoals"]["host"]} - {match["matchGoals"]["guest"]} {match["guestName"]}\n'
        return matches
