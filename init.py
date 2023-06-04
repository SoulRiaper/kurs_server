from MainUi import MainUi
from PyQt5.QtWidgets import QApplication
import sys
from DataRepository import DataRepository

app = QApplication(sys.argv)

window = MainUi(DataRepository())

window.show()
app.exec()
