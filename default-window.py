from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

class DefualtWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wind & Water")
        self.setGeometry(200, 50, 600, 700)
        
        self.UiComponents()


    def UiComponents(self):
        title = QLabel("Wind and Water", self)
        label = QLabel("Second Line", self)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(label)
        layout.addStretch()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DefualtWindow()
    #window = uic.loadUi("Ui/mainwindow.ui")
    window.show()
    sys.exit(app.exec())
