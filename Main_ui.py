# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(635, 503)
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(140, 10, 311, 51))
        self.label_title.setStyleSheet("font: 25pt \"方正小标宋简体\";\n"
"color: rgb(0, 0, 0);")
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setScaledContents(False)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setWordWrap(False)
        self.label_title.setObjectName("label_title")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 280, 481, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        self.Button_left = QtWidgets.QPushButton(Form)
        self.Button_left.setGeometry(QtCore.QRect(120, 420, 111, 41))
        self.Button_left.setObjectName("Button_left")
        self.Button_right = QtWidgets.QPushButton(Form)
        self.Button_right.setGeometry(QtCore.QRect(350, 420, 111, 41))
        self.Button_right.setObjectName("Button_right")
        self.label_1_left = QtWidgets.QLabel(Form)
        self.label_1_left.setGeometry(QtCore.QRect(70, 80, 271, 31))
        self.label_1_left.setStyleSheet("font: 11pt \"方正小标宋简体\";")
        self.label_1_left.setObjectName("label_1_left")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(70, 110, 481, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2_left = QtWidgets.QLabel(Form)
        self.label_2_left.setGeometry(QtCore.QRect(70, 240, 501, 31))
        self.label_2_left.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 11pt \"方正小标宋简体\";")
        self.label_2_left.setText("")
        self.label_2_left.setObjectName("label_2_left")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "打字训练器"))
        self.label_title.setText(_translate("Form", "打字训练器"))
        self.Button_left.setText(_translate("Form", "提交"))
        self.Button_right.setText(_translate("Form", "下一句"))
        self.label_1_left.setText(_translate("Form", "此次训练的句子为："))
