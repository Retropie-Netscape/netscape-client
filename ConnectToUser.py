import json
import GetUserInfo
import UpdateServerUserInfo


def write_connection_details(username: str):

    jsondata = GetUserInfo.get_connection_details(username)

    if jsondata is None:
        return 1

    else:
        with open('/opt/retropie/configs/all/retronetplay.cfg', 'a+') as netplayconfigfile:
            netplayconfigfile.truncate(0)
            lines = ['__netplaymode="C"\n', '__netplayport="' + jsondata['port'] + '"\n',
            '__neplayhostip="' + jsondata['ipAddress'] + '"\n', '__netplayip_cfile=""\n',
                     '__netplaynickname="' + username + '"\n']
            netplayconfigfile.writelines(lines)

    return 0


if __name__ == '__main__':
    write_connection_details()