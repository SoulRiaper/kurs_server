from UI_MainWindow import Ui_MainWindow
import serial
from serial.tools.list_ports import comports
from PyQt5.QtCore import QTimer
from DataRepository import DataRepository
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import random

class MainUi(QMainWindow):

      def __init__(self, db: DataRepository) -> None:
            super().__init__()
            
            # Define Window UI components
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.startStopButton.clicked.connect(self.startListen)
            self.ui.ListenPortButton.clicked.connect(self.setupPort)

            # Define database module
            self.db = db

            # Define message box to handle exceptions
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.listenPort)

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

      
      def setupPort(self):
            try:      
                  self.s = serial.Serial(
                        port = str(self.ui.comPorts.currentText()),
                        baudrate = int(self.ui.SpeedValue.currentText()),
                        bytesize = int(self.ui.LengthValue.currentText()),
                        
                        )
                  self.showMessageBox("OK", "Соединение установлено")

            except serial.SerialException as e:
                  self.showMessageBox(e.__class__.__name__, str(e))
            
      def showMessageBox(self, title: str, text: str):
            self.msg.setWindowTitle(title)
            self.msg.setText(text)
            self.msg.exec_()

      # Method starts listening (on button click)
      def startListen(self):
            self.timer.start(1000)
            self.ui.startStopButton.setText("Остановить мониторинг")
            self.ui.startStopButton.clicked.connect(self.stopListen)

      # Method stop listening (on button click)
      def stopListen(self):
            self.timer.stop()
            self.ui.startStopButton.setText("Начать мониторинг")
            self.ui.startStopButton.clicked.connect(self.startListen)

