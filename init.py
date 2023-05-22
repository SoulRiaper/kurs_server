from MainUi import MainUi
from ports import ports
from qtpy.QtWidgets import QMainWindow, QApplication
import sys

app = QApplication(sys.argv)
window = QMainWindow()
ui = MainUi()

ui.setupUi(window)

window.show()
app.exec()