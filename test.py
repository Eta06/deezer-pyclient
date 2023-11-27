from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QMovie, QTextOption
from PyQt5.QtWidgets import QApplication
import deezertools as deezer

user = deezer.init()

app = QApplication([])

window = uic.loadUi("test.ui")  # Load the PyQt UI file

# Get the upperlayout from the PyQt UI file
upperLayout = window.upperLayout

# set maximum height for each widget in the layout
for i in range(upperLayout.count()):
    widget = upperLayout.itemAt(i).widget()
    if widget is not None:
        widget.setMaximumHeight(40)


window.show()
app.exec_()