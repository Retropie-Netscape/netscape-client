import requests
import json
import sqlite3


url = 'https://10.0.0.119:5000/user'


def get_connection_details(username: str):
    data = {
        "username": '\'' + username + '\''
    }

    r = requests.get(url, params=data, verify=False)
    jsondata = r.json()

    if jsondata['serverCode'] == 400:
        print("ERROR: Could not find user with name: " + username + " in server database.")
        return None

    else:
        return jsondata


##
# Gets all user info from server. Meant to be primarily used when adding a new user to the local database
def get_user_details(username: str):
    data = {
        'username': '\'' + username + '\''
    }

    r = requests.get(url=url, params=data, verify=False)
    jsondata = r.json()

    if jsondata['serverCode'] == 400:
        print("ERROR: Could not find user with name: " + username + " in server database.")

    else:
        with open(username + '.json', 'w') as userfile:
            json.dump(jsondata, userfile)
