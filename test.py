from PyQt5 import uic
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication

app = QApplication([])
window = uic.loadUi("test.ui")  # PyQt Designer ile oluturulan .ui dosyanızın adını yazınız.



window.show()
app.exec_()