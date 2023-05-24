from MainUi import MainUi
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
import sys
from DataRepository import DataRepository

app = QApplication(sys.argv)

window = MainUi(DataRepository())

# timer = QTimer(window)
# timer.timeout.connect(window.listenPort)
# timer.start(1000)

window.show()
app.exec()