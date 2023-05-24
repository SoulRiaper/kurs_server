from UI_MainWindow import Ui_MainWindow
import serial
from serial.tools.list_ports import comports
from DialogUi import DialogUi
from PyQt5.QtWidgets import QDialog
import serial.tools.list_ports as list_ports
from DataRepository import DataRepository

class MainUi(Ui_MainWindow):

      def __init__(self, db: DataRepository) -> None:
            super().__init__()
            self.db = db

      def setupUi(self, MainWindow):
            super().setupUi(MainWindow)
            self.portListenButton.clicked.connect(self.setupPort)
            self.ListenPortButton.clicked.connect(self.listenPort)

            dialog = DialogUi()
            dialog_ui = QDialog()
            dialog.setupUi(dialog_ui)
            self.dialog = dialog_ui


      def listenPort(self):
            
            while 1:
                  
                  if self.s.in_waiting > 0:
                        string = self.s.read(16).decode('utf-8', 'ignore')
                        
                        try:
                              self.LastValue.setText(repr(string))
                        except Exception as ex:
                              print(ex)
                              pass


      def setupPort(self):
            self.s = serial.Serial(
                  port = str(self.comPorts.currentText()),
                  baudrate = int(self.SpeedValue.currentText()),
                  bytesize = int(self.LengthValue.currentText()),
                  
                  )
            self.LastValue.setText('123123123')

      def show_comPort_window(self):
            self.dialog.show()

      def retranslateUi(self, MainWindow):
            super().retranslateUi(MainWindow)
            ports = comports()
            if len(ports) == 0:
                  return
            for port in ports:
                  self.comPorts.addItem(port.device)