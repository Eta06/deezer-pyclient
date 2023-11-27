from PyQt5 import uic
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication
import deezertools as deezer

# Deezer API
arl_token = deezer.read_arl_token()
session_token, user_id = deezer.authenticate_user(arl_token)
playlists = deezer.get_user_playlists(session_token, user_id)
user_info = deezer.get_user_info(session_token, user_id)
print(user_info)

app = QApplication([])

window = uic.loadUi("test.ui")  # Load the PyQt UI file

window.show()
app.exec_()
