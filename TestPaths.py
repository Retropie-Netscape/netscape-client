import ConnectToUser


def test_write_connection_details():
    ConnectToUser.write_connection_details('TestTEster')


def test_update_user():
    ConnectToUser.push_user_data()


if __name__ == "__main__":
    #test_update_user()
    test_write_connection_details()