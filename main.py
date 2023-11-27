import deezertools as deezer
from PyQt5 import QtCore, QtGui, QtWidgets


def main():
    # Read arl token from json file
    arl_token = deezer.read_arl_token()

    session_token, user_id = deezer.authenticate_user(arl_token)

    if session_token and user_id:
        playlists = deezer.get_user_playlists(session_token, user_id)

        if playlists:
            print(playlists)


if __name__ == "__main__":
    main()
