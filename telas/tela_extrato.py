# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extrato.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 480)
        Form.setStyleSheet("background-color: rgb(196, 215, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(190, 100, 301, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color: rgb(196, 215, 255,0.5);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 299, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextHistorico = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.TextHistorico.setText("")
        self.TextHistorico.setObjectName("TextHistorico")
        self.verticalLayout.addWidget(self.TextHistorico)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ButtonSair = QtWidgets.QPushButton(Form)
        self.ButtonSair.setGeometry(QtCore.QRect(350, 400, 80, 23))
        self.ButtonSair.setStyleSheet("background-color: rgb(255, 0, 0, 0);")
        self.ButtonSair.setObjectName("ButtonSair")
        self.ButtonVoltar = QtWidgets.QPushButton(Form)
        self.ButtonVoltar.setGeometry(QtCore.QRect(260, 400, 80, 23))
        self.ButtonVoltar.setStyleSheet("background-color: rgb(171, 200, 206,0);")
        self.ButtonVoltar.setObjectName("ButtonVoltar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Extrato"))
        self.label_6.setText(_translate("Form", "NyBank"))
        self.ButtonSair.setText(_translate("Form", "Sair"))
        self.ButtonVoltar.setText(_translate("Form", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())