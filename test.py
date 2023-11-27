from PyQt5 import uic
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication

app = QApplication([])
window = uic.loadUi("test.ui") # Load the PyQt UI file


window.show()
app.exec_()