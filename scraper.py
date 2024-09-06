import requests
from langchain_openai import ChatOpenAI



def get_matches_data():
    data = []
    for day in range(-2, 1):
        API_URL_MATCHES = f"https://web-api.varzesh3.com/v1.0/livescore/{day}"
        r = requests.get(API_URL_MATCHES)
        if r.status_code == 200:
            data += r.json()["matches"]
    return data



def get_game_result(team1, team2):
    data = get_matches_data()
    for match in data:
        if match["hostName"] == team1 and match["guestName"] == team2:
            return f'{match["hostName"]} {match["matchGoals"]["host"]} - {match["matchGoals"]["guest"]} {match["guestName"]}'
        elif match["hostName"] == team2 and match["guestName"] == team1:
            return f'{match["hostName"]}{match["matchGoals"]["host"]}-{match["matchGoals"]["guest"]}{match["guestName"]}'

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

def gpt_API(message):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        base_url="https://api.avalai.ir/v1",
        api_key="aa-88oVsr7AaMIQj3GTbMnXbLT4yY9LDUNeCBO5HRzlCOrbaTy8")

    return llm.invoke("can i talk with you?").content


