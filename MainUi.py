from UI_MainWindow import Ui_MainWindow
import serial
from serial.tools.list_ports import comports
from PyQt5.QtCore import QTimer
from DataRepository import DataRepository
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from SerialReader import SerialReader
import random

class MainUi(QMainWindow):

      def __init__(self, db: DataRepository) -> None:
            super().__init__()
            
            # Define Window UI components
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.startStopButton.clicked.connect(self.listenPort)
            # Define database module
            self.db = db

            # Define message box to handle exceptions
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)

            ports = comports()
            if len(ports) == 0:
                  return
            for port in ports:
                  self.ui.comPorts.addItem(port.device)


      def listenPort(self):
            try:
                  
                  self.serial_reader = SerialReader(
                        port = str(self.ui.comPorts.currentText()),
                        baudrate = int(self.ui.SpeedValue.currentText()),
                        byte_size = int(self.ui.LengthValue.currentText()),
                  )
                  
            except serial.SerialException as e:
                  self.showMessageBox(f"ERROR: {e.__class__.__name__}", str(e))
                  
            self.serial_reader.new_data.connect(self.handle_data)
            self.serial_reader.start()

      def handle_data(self, data):
            data = data.split()
            data[:] = [round((float(val) * 3.3 / 4095), 2) for val in data]
            self.ui.LastValue.setText(str(data[0]))
            self.db.insertVoltageValue(data[0])
            
                   
      def showMessageBox(self, title: str, text: str):
            self.msg.setWindowTitle(title)
            self.msg.setText(text)
            self.msg.exec_()
