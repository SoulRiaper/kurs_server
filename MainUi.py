from UI_MainWindow import Ui_MainWindow
from serial.tools.list_ports import comports
from DialogUi import DialogUi
from PyQt6.QtWidgets import QDialog
import random
from DataRepository import DataRepository

class MainUi(Ui_MainWindow):

      def __init__(self, db: DataRepository) -> None:
            super().__init__()
            self.db = db

      def setupUi(self, MainWindow):
            super().setupUi(MainWindow)
            self.portListenButton.clicked.connect(self.show_comPort_window)
            self.ListenPortButton.clicked.connect(self.updateValue)

            dialog = DialogUi()
            dialog_ui = QDialog()
            dialog.setupUi(dialog_ui)
            self.dialog = dialog_ui

      def updateValue(self, value: int):
            value = random.randint(0, 10)
            self.LastValue.setText(str(value))
            self.db.insertVoltageValue(value)

      def show_comPort_window(self):
            self.dialog.show()

      def retranslateUi(self, MainWindow):
            super().retranslateUi(MainWindow)
            ports = comports()
            if len(ports) == 0:
                  return
            for port in ports:
                  self.comPorts.addItems(port.name)