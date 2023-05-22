from window import Ui_MainWindow
import serial.tools.list_ports as list_ports

class MainUi(Ui_MainWindow):
    
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        ports = list_ports.comports()
        for port in ports:
            self.comPorts.addItems(port)