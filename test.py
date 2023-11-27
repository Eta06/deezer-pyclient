from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication
import deezertools as deezer


user = deezer.init()

app = QApplication([])

window = uic.loadUi(f"test.ui".format())  # Load the PyQt UI file

window.show()
app.exec_()
