import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Araç Çubuğu oluştur
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        # Araç Çubuğuna Ekle Butonları
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)

        fullscreenAction = QAction('Fullscreen', self)
        fullscreenAction.triggered.connect(self.toggle_fullscreen)

        toolbar.addAction(exitAction)
        toolbar.addAction(fullscreenAction)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Toolbar Example')

    def toggle_fullscreen(self):
        # Fullscreen modunu aç/kapat
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

def main():
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
