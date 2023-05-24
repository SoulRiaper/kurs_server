from UI_MainWindow import Ui_MainWindow
import serial
from serial.tools.list_ports import comports
from PyQt5.QtCore import QTimer
from DataRepository import DataRepository
from PyQt5.QtWidgets import QMainWindow
import random

class MainUi(QMainWindow):

      def __init__(self, db: DataRepository) -> None:
            super().__init__()

            self.ui = Ui_MainWindow()
            
            self.ui.setupUi(self)
            self.ui.startStopButton.clicked.connect(self.startListen)

            self.db = db

            ports = comports()
            if len(ports) == 0:
                  return
            for port in ports:
                  self.ui.comPorts.addItem(port.device)

      def listenPort(self):
            self.ui.LastValue.setText(f"{random.randint(0,10)}")
            # if self.s.in_waiting > 0:
            #       string = self.s.read(16).decode('utf-8', 'ignore')
                  
            #       try:
            #             self.LastValue.setText(repr(string))
            #       except Exception as ex:
            #             print(ex)
            #             pass


      def startListen(self):
            self.timer.start(1000)
            self.ui.startStopButton.setText("Остановить мониторинг")
            self.ui.startStopButton.clicked.connect(self.stopListen)

      def stopListen(self):
            self.timer.stop()
            self.ui.startStopButton.setText("Начать мониторинг")
            self.ui.startStopButton.clicked.connect(self.startListen)

      def setupPort(self):
            self.s = serial.Serial(
                  port = str(self.comPorts.currentText()),
                  baudrate = int(self.SpeedValue.currentText()),
                  bytesize = int(self.LengthValue.currentText()),
                  
                  )
            self.LastValue.setText('123123123')
            

      def show(self) -> None:
            super().show()
            # self.startStopButton.clicked.connect(self.startListen)
            
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.listenPort)
            