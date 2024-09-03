import requests


def get_matches_data():
    data = []
    for day in range(-2, 1):
        API_URL_MATCHES = f"https://web-api.varzesh3.com/v1.0/livescore/{day}"
        r = requests.get(API_URL_MATCHES)
        if r.status_code == 200:
            data += r.json()["matches"]
    return data



def get_game_result(team1, team2):
    data = get_data()
    for match in data:
        if match["hostName"] == team1 and match["guestName"] == team2:
            return f'{match["hostName"]} {match["matchGoals"]["host"]} - {match["matchGoals"]["guest"]} {match["guestName"]}'
        elif match["hostName"] == team2 and match["guestName"] == team1:
            return f'{match["hostName"]}{match["matchGoals"]["host"]}-{match["matchGoals"]["guest"]}{match["guestName"]}'

def get_news_title():
    data = []
    titles  = []
    API_URL_NEWS = "https://web-api.varzesh3.com/v1.0/news/most-commented?includeSports[0]=Football&includeSports[1]=Futsal&includeSports[2]=BeachSoccer"
    request = requests.get(API_URL_NEWS)
    data += request.json()
    if request.status_code == 200:
        for object in data:
            titles.append(object["title"])
        return return f"{titles[0]}\n{titles[1]}\n{titles[2]}\n{titles[3]}\n{titles[4]}"
