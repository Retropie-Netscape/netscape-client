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
        with open('friends/' + username + '.json', 'a+') as newuserfile:
            userexists = False
            for line in newuserfile.readlines():
                if line.__contains__(username):
                    userexists = True

            if not userexists:
                newuserfile.write(username)


def update_user_info(username: str, ipaddress: str, port: str, hostmode: str):
    updatedata = {
        'username': '\'' + username + '\'',
        'ipAddress': '\'' + ipaddress + '\'',
        'port': '\'' + port + '\'',
        'mode': '\'' + hostmode + '\''
    }

    r = requests.put(url='https://10.0.0.119:5000/user/connection-details', json=updatedata, verify=False)
    jsondata = r.json()

    if jsondata['serverCode'] == 400:
        print('ERROR: Necessary user data was not correctly formatted for the server. Check that data is formatted correctly')
        return None
    else:
        return 0


def update_leaderboard_info(username: str, mostplayedgame: str, mostplayedsystem: str)
    updatedata = {
        'username': '\'' + username + '\'',
        'mostPlayedGame': '\'' + mostplayedgame + '\'',
        'mostPlayedSystem': '\'' + mostplayedsystem + '\'',
    }

    r = requests.put(url='https://10.0.0.119:5000/user/leaderboard-details', json=updatedata, verify=False)
    jsondata = r.json()

    if jsondata['serverCode'] == 400:
        print(
            'ERROR: Necessary new user data was not correctly formatted for the server. Check that data is formatted correctly')
        return None
    else:
        return 0