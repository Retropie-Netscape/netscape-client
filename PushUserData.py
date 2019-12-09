import UpdateServerUserInfo


def push_user_data():
    port = None
    ip = None
    username = None
    hostingmode = None
    with open('/opt/retropie/configs/all/retronetplay.cfg', 'r') as netplayconfigfile:
        for line in netplayconfigfile:
            if line.__contains__('__netplayport='):
                port = line.__str__()
                port.replace("__netplayport=", "")
            elif line.__contains__('__netplayhostip='):
                ip = line.__str__()
                ip.replace("__netplayhostip=", "")
            elif line.__contains__('__netplaynickname='):
                username = line.__str__()
                username.replace('__netplaynickname=', "")
            elif line.__contains__('__mode='):
                hostingmode = line.__str__()
                hostingmode.replace("__netplaymode=", "")

    if username.__contains__('"RetroPie"'):
        print('Please enter a nickname that you would like for your account:\n')
        username = input()
        with open('/opt/retropie/configs/all/retronetplay.cfg', 'a+') as netplayconfigfile:
            i = 0
            for line in netplayconfigfile.readlines():
                i += 1
                if line.__contains__('__nickname'):
                    netplayconfigfile.truncate(i)
                    netplayconfigfile.write('__nickname="' + username + '"')
        UpdateServerUserInfo.create_user(username, ip.__str__(), port.__str__(), hostingmode.__str__())
    else:
        UpdateServerUserInfo.update_user_info(username.__str__(), ip.__str__(), port.__str__(), hostingmode.__str__())

    print('Data successfully sent to the server')


if __name__ == '__main__':
    push_user_data()
