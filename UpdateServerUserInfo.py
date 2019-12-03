import requests
import json


def create_user(username: str, ipaddress: str, port: str, hostingmode: str):
    newuserdata = {
        'username': '\'' + username + '\'',
        'ipAddress': '\'' + ipaddress + '\'',
        'port': '\'' + port + '\'',
        'mode': '\'' + hostingmode + '\''
    }

    r = requests.post(url='https://10.0.0.119:5000/user', json=newuserdata, verify=False)
    jsondata = r.json()

    if jsondata['serverCode'] == 400:
        print('ERROR: Necessary new user data was not correctly formatted for the server. Check that data is formatted correctly')
        return None

    else:
        with open('./friends/' + username + '.json', 'w') as newuserfile:
            json.dump(jsondata, newuserfile)


def update_user_info(username: str, mostplayedgame: str, mostplayedsystem: str):
    updatedata = {
        'username': '\'' + username + '\'',
        'mostPlayedGame': '\'' + mostplayedgame + '\'',
        'mostPlayedSystem': '\'' + mostplayedsystem + '\''
    }

    r = requests.put(url='https://10.0.0.119:5000/user/leaderboard-details', json=updatedata, verify=False)
    jsondata = r.json()

    if jsondata['serverCode'] == 400:
        print('ERROR: Necessary new user data was not correctly formatted for the server. Check that data is formatted correctly')
        return None
    else:
        return
