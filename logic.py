# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:      logic
# Date:      2020/3/26
__Author__ = 'Negoo_wen'
#-------------------------------------------------------------------------------

import sys
from random import randint
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from Main_ui import Ui_Form
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


class MyForm(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(MyForm, self).__init__()
        self.setupUi(self)
        self.window1 = uic.loadUi("Main_ui.ui")
        self.window1.Button_left.clicked.connect(self.submit)
        self.window1.Button_right.clicked.connect(self.next_one)
        self.text_show()
        #a = "While there is life, there is hope."
        #self.window1.textBrowser.setText(a)

    def submit(self):
        text1 = self.window1.textBrowser.toPlainText()
        text2 = self.window1.textEdit_2.toPlainText()
        count = 0
        for i in range(len(text1)):
            try:
                if text1[i] == text2[i]:
                    count += 1
            except Exception as e:
                QMessageBox.about(self.window1,'警告','与源文本长度不同，请细心输入！')
                break
        accuracy = count / len(text1) *100
        print(accuracy)
        info = "有点可惜，你的正确率是: %.2f%% " % accuracy if accuracy != 100 else "恭喜你全对了呢！100分！继续加油哦！"
        self.window1.label_2_left.setText(info)
        #self.Button_left.setShortcut('Ctrl + e')

    def text_show(self):
        all_1 = self.read_dic()
        text_a = all_1[randint(1,len(all_1))]
        self.window1.textBrowser.setText(text_a)

    def read_dic(self):
        f = open('text.dic', 'r')  # 文件为123.txt
        sourceInLines = f.readlines()  # 按行读出文件内容
        f.close()
        all_text = []  # 定义一个空列表，用来存储结果
        for line in sourceInLines:
            temp1 = line.strip('\n')
            all_text.append(temp1)
        return all_text

    def next_one(self):
        self.text_show()
        self.window1.textEdit_2.setText('')

if __name__ == '__main__':
    app = QApplication([])
    stats = MyForm()
    stats.window1.show()
    app.exec_()