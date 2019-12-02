import json
import GetUserInfo
import UpdateServerUserInfo


def write_connection_details():
    username = None
    with open('/opt/retropie/configs/all/retronetplay.cfg', 'w+') as netplayconfigfile:
        username = netplayconfigfile.read(4)

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

def get_connection_details():
    port = None
    ip = None
    username = None
    hostingmode = None
    with open('/opt/retropie/configs/all/retronetplay.cfg', 'r') as netplayconfigfile:
        for line in netplayconfigfile:
            if line.__contains__('__netplayport='):
                port = line.replace("__netplayport=", "")
            elif line.__contains__('__netplayhostip='):
                ip = line.replace("__netplayhostip=", "")
            elif line.__contains__('__nickname='):
                username = line.replace('__nickname=', "")
            elif line.__contains__('__mode='):
                hostingmode = line.replace("__mode=", "")

    if username.__str__() == '"RetroPie"':
        username = input(__prompt='Please enter a nickname that you would like for your account:\n')
        UpdateServerUserInfo.create_user(username, ip.__str__(), port.__str__(), hostingmode.__str__())
    else:
        UpdateServerUserInfo.create_user(username.__str__(), ip.__str__(), port.__str__(), hostingmode.__str__())

    print('Data successfully sent to the server')

