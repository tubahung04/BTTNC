# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 370, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_plaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(200, 160, 351, 81))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_ciphertext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(200, 340, 351, 81))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.btn_en = QtWidgets.QToolButton(self.centralwidget)
        self.btn_en.setGeometry(QtCore.QRect(190, 470, 91, 41))
        self.btn_en.setObjectName("btn_en")
        self.btn_de = QtWidgets.QToolButton(self.centralwidget)
        self.btn_de.setGeometry(QtCore.QRect(420, 470, 91, 41))
        self.btn_de.setObjectName("btn_de")
        self.txt_infor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_infor.setGeometry(QtCore.QRect(730, 160, 351, 81))
        self.txt_infor.setObjectName("txt_infor")
        self.txt_signature = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(730, 330, 351, 81))
        self.txt_signature.setObjectName("txt_signature")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 170, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_sign = QtWidgets.QToolButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(730, 470, 91, 41))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QToolButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(980, 470, 91, 41))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_generate = QtWidgets.QToolButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(220, 90, 91, 41))
        self.btn_generate.setObjectName("btn_generate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text"))
        self.btn_en.setText(_translate("MainWindow", "Encrypt"))
        self.btn_de.setText(_translate("MainWindow", "Decrypt"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_generate.setText(_translate("MainWindow", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
