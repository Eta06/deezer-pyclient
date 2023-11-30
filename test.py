from PyQt5 import uic, QtWidgets, QtGui, QtNetwork, QtCore
from PyQt5.QtGui import QMovie, QTextOption
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import deezertools as deezer
import ButtonHandler

user = deezer.init()
print("Starting App With:", user)

language = user["language"]
theme = user["theme"]
playlists = user["playlists"]
# Remove unnecessary keys from playlists
for playlist in playlists:
    for key in list(playlist.keys()):
        if key not in ["title", "id", "picture", "duration", "nb_tracks", "fans", "public", "collaborative", "link", "picture_small", "tracklist", "creation_date"]:
            del playlist[key]

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

# <widget class="QListWidget" name="listWidget"> isimli widget'ın içine AnaSayfa, Keşfet, Kütüphane ve Sevilenler butonlarını ekler
listWidget = window.findChild(QtWidgets.QListWidget, 'listWidget')

button_names = ["Ana sayfa", "Keşfet", "Kütüphane", "Sevilenler"]
button_icons = ["./assets/" + theme + "/home.png", "./assets/" + theme + "/explore.png",
                "./assets/" + theme + "/library2.0.png", "./assets/" + theme + "/favourites.png"]

# Check if listWidget exists
if listWidget is not None:
    # Create QPushButton elements and add them to the QListWidget
    for button_name, button_icon in zip(button_names, button_icons):
        button_name = " " + button_name  # Add space characters to the button name for padding

        # Create a QListWidgetItem
        item = QtWidgets.QListWidgetItem()

        # Create a QPushButton
        button = QtWidgets.QPushButton(button_name)

        # Set the font size
        font = button.font()
        font.setPointSize(20)  # 14 is the font size
        button.setFont(font)

        # Set the icon
        icon = QtGui.QIcon(button_icon)
        button.setIcon(icon)
        # 24,24 is the icon size
        button.setIconSize(QtCore.QSize(24, 24))
        button.setFixedHeight(50)
        button.setStyleSheet(
            """
            QPushButton {
                text-align:left; 
                padding:0; 
                font-weight:bold; 
                padding-top: 10px;
                padding-bottom: 10px;
                margin-bottom: 2px;
                padding-left: 10px;
                padding-right: 10px;
                font-size:20px;
            }
            QPushButton:hover {
                border: 1px solid #BBBBBB;
            }
            QPushButton:pressed {
                border: 2px solid #BBBBBB;
            }
            """)
        button.setFlat(True)

        # Set the size of the QListWidgetItem
        item.setSizeHint(button.sizeHint())

        # Add the QListWidgetItem to the QListWidget
        listWidget.addItem(item)

        # Set the QPushButton as the widget for the QListWidgetItem
        listWidget.setItemWidget(item, button)

    # Create a new Scrollable Area
    scrollArea = QtWidgets.QScrollArea()
    scrollArea.setWidgetResizable(True)
    scrollArea.setFixedHeight(150)

    # Create container and layout for the widgets inside scroll
    container = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(container)

    # add label as example, you can add any widget here
    label = QtWidgets.QLabel("Hello Scroll Part!")
    layout.addWidget(label)

    scrollArea.setWidget(container)

    # Add the Scrollable Area to QListWidget
    scroll_item = QtWidgets.QListWidgetItem(listWidget)
    listWidget.setItemWidget(scroll_item, scrollArea)

    # Kütüphane butonuna tıklandığında ButtonHandler.py dosyasındaki libraryhandler fonksiyonunu çalıştırır
    library_button = listWidget.itemWidget(listWidget.item(2))
    print(library_button)
    library_button.clicked.connect(ButtonHandler.libraryhandler(window))



else:
    print("No widget named 'listWidget' found")

window.show()
app.exec_()