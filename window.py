# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comPorts = QtWidgets.QComboBox(self.centralwidget)
        self.comPorts.setObjectName("comPorts")
        self.gridLayout.addWidget(self.comPorts, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LengthValue = QtWidgets.QComboBox(self.centralwidget)
        self.LengthValue.setObjectName("LengthValue")
        self.LengthValue.addItem("")
        self.LengthValue.addItem("")
        self.gridLayout.addWidget(self.LengthValue, 2, 1, 1, 1)
        self.SpeedValue = QtWidgets.QComboBox(self.centralwidget)
        self.SpeedValue.setObjectName("SpeedValue")
        self.SpeedValue.addItem("")
        self.SpeedValue.addItem("")
        self.SpeedValue.addItem("")
        self.SpeedValue.addItem("")
        self.SpeedValue.addItem("")
        self.gridLayout.addWidget(self.SpeedValue, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система сбора данных"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Скорость:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Длинна:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Создать файл конфигурации"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">COM PORT:</span></p></body></html>"))
        self.LengthValue.setItemText(0, _translate("MainWindow", "8"))
        self.LengthValue.setItemText(1, _translate("MainWindow", "9"))
        self.SpeedValue.setItemText(0, _translate("MainWindow", "115200"))
        self.SpeedValue.setItemText(1, _translate("MainWindow", "19200"))
        self.SpeedValue.setItemText(2, _translate("MainWindow", "57600"))
        self.SpeedValue.setItemText(3, _translate("MainWindow", "9600"))
        self.SpeedValue.setItemText(4, _translate("MainWindow", "4800"))
