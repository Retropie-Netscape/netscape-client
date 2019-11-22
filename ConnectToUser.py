import json
import GetUserInfo

def write_connection_details(username: str):
    jsondata = GetUserInfo.get_connection_details(username)

    if jsondata is None:
        return None

    else: