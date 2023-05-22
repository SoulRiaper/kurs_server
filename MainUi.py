from UI_MainWindow import Ui_MainWindow
from serial.tools.list_ports import comports

class MainUi(Ui_MainWindow):
    
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        ports = comports()
        if len(ports) == 0:
            return
        for port in ports:
            self.comPorts.addItems(port.name)