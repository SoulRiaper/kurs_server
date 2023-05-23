from MainUi import MainUi
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from DataRepository import DataRepository

app = QApplication(sys.argv)
window = QMainWindow()
ui = MainUi(db=DataRepository())

ui.setupUi(window)

window.show()
app.exec()