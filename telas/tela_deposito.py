# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_deposito.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Form.setStyleSheet("background-color: rgb(196, 215, 255);\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineSaldo = QtWidgets.QLineEdit(Form)
        self.lineSaldo.setGeometry(QtCore.QRect(300, 190, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineSaldo.setFont(font)
        self.lineSaldo.setStyleSheet("background-color: rgb(196, 215, 255, 0.5);")
        self.lineSaldo.setObjectName("lineSaldo")
        self.ButtonDepositar = QtWidgets.QPushButton(Form)
        self.ButtonDepositar.setGeometry(QtCore.QRect(350, 270, 80, 23))
        self.ButtonDepositar.setStyleSheet("background-color: rgb(171, 200, 206,0);")
        self.ButtonDepositar.setObjectName("ButtonDepositar")
        self.ButtonSair = QtWidgets.QPushButton(Form)
        self.ButtonSair.setGeometry(QtCore.QRect(490, 390, 80, 23))
        self.ButtonSair.setStyleSheet("background-color: rgb(255, 0, 0, 0);")
        self.ButtonSair.setObjectName("ButtonSair")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ButtonVoltar = QtWidgets.QPushButton(Form)
        self.ButtonVoltar.setGeometry(QtCore.QRect(380, 390, 80, 23))
        self.ButtonVoltar.setStyleSheet("background-color: rgb(171, 200, 206,0);")
        self.ButtonVoltar.setObjectName("ButtonVoltar")
        self.labelNotificacao = QtWidgets.QLabel(Form)
        self.labelNotificacao.setGeometry(QtCore.QRect(250, 300, 221, 20))
        self.labelNotificacao.setObjectName("labelNotificacao")
        self.lineSaldo_2 = QtWidgets.QLineEdit(Form)
        self.lineSaldo_2.setGeometry(QtCore.QRect(300, 230, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineSaldo_2.setFont(font)
        self.lineSaldo_2.setStyleSheet("background-color: rgb(196, 215, 255, 0.5);")
        self.lineSaldo_2.setObjectName("lineSaldo_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 230, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Depósito"))
        self.label_2.setText(_translate("Form", "Valor do depósito : "))
        self.ButtonDepositar.setText(_translate("Form", "Depositar"))
        self.ButtonSair.setText(_translate("Form", "Sair"))
        self.label_3.setText(_translate("Form", "NyBank"))
        self.ButtonVoltar.setText(_translate("Form", "Voltar"))
        self.labelNotificacao.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("Form", " Número conta : "))