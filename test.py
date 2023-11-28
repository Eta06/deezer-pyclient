from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie, QTextOption
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
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

button_names = ["AnaSayfa", "Keşfet", "Kütüphane", "Sevilenler"]
button_icons = ["./assets/play_button_white.png", ":/assets/play_button_white.png", ":/assets/play_button_white.png", ":/assets/play_button_white.png"]

# Check if listWidget exists
if listWidget is not None:
    # Create QPushButton elements and add them to the QListWidget
    for button_name, button_icon in zip(button_names, button_icons):
        # Create a QListWidgetItem
        item = QtWidgets.QListWidgetItem()

        # Create a QPushButton
        button = QtWidgets.QPushButton(button_name)

        # Set the font size
        font = button.font()
        font.setPointSize(14)  # 14 is the font size
        button.setFont(font)

        # Set the icon
        icon = QtGui.QIcon(button_icon)
        button.setIcon(icon)
        # 24,24 is the icon size
        button.setIconSize(QtCore.QSize(24, 24))
        button.setStyleSheet("text-align:left;")
        button.setFlat(True)

        # Set the size of the QListWidgetItem
        item.setSizeHint(button.sizeHint())

        # Add the QListWidgetItem to the QListWidget
        listWidget.addItem(item)

        # Set the QPushButton as the widget for the QListWidgetItem
        listWidget.setItemWidget(item, button)
else:
    print("No widget named 'listWidget' found")


window.show()
app.exec_()