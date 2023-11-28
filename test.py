from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtGui import QMovie, QTextOption
from PyQt5.QtWidgets import QApplication
import deezertools as deezer

user = deezer.init()

app = QApplication([])

window = uic.loadUi("test.ui")  # Load the PyQt UI file

# Print the object names of all the layouts in the window
for layout in window.findChildren(QtWidgets.QLayout):
    print(layout.objectName())

upperLayout = window.findChild(QtWidgets.QHBoxLayout, 'horizontal_layout1')

if upperLayout is not None:
    # Set maximum height for each widget in the layout
    for i in range(upperLayout.count()):
        widget = upperLayout.itemAt(i).widget()
        if widget is not None:
            widget.setMaximumHeight(40)
else:
    print("No layout named 'horizontal_layout1' found")

# <widget class="QListWidget" name="listWidget"> isimli widget'ın içine AnaSayfa, Keşfet, Kütüphane ve Sevilenler butonlarını ekler
listWidget = window.findChild(QtWidgets.QListWidget, 'listWidget')


window.show()
app.exec_()