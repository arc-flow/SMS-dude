import requests


def get_data():
    data = []
    for day in range(-2, 1):
        API_URL = f"https://web-api.varzesh3.com/v1.0/livescore/{day}"
        r = requests.get(API_URL)
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
