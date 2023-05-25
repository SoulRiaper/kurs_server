import serial
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time

class SerialReader(QThread):
    
    new_data = pyqtSignal(str)
    
    def __init__(self, port, baudrate: int, byte_size = 8) -> None:
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.byte_size = byte_size
        self.serial_port = None    
    
    def run(self) -> None:
        self.serial_port = serial.Serial(
            self.port,
            self.baudrate,
            self.byte_size
            )
        
        while True:
            if self.serial_port.in_waiting > 0:
                
                data = self.serial_port.readline().decode('utf-8', 'ignore')
                
                self.new_data.emit(data)
            time.sleep(0.1)
    
    
    def stop(self):
        
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()