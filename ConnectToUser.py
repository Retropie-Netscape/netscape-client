import json
import GetUserInfo
import UpdateServerUserInfo


def write_connection_details(username: str):

    jsondata = GetUserInfo.get_connection_details(username)

    if jsondata is None:
        return 1

    else:
        with open('/opt/retropie/configs/all/retronetplay.cfg', 'w+') as netplayconfigfile:
            line4 = netplayconfigfile.readline(3)
            line5 = netplayconfigfile.readline(4)
            lines = ['__netplaymode="C"', '__netplayport="' + jsondata['port'] + '"',
            '__neplayhostip="' + jsondata['ipAddress'] + '"', line4, line5]
            netplayconfigfile.writelines(lines)

    return 0


if __name__ == '__main__':
    write_connection_details()