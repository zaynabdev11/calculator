# -*- coding: utf-8 -*-
# 2019
# Form implementation generated from reading ui file 'calculatrice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(328, 509)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(328, 509))
        MainWindow.setMaximumSize(QtCore.QSize(328, 509))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(10, 310, 70, 70))
        self.button_1.setStyleSheet("color:rgb(12, 12, 12);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(90, 310, 70, 70))
        self.button_2.setStyleSheet("color:rgb(12, 12, 12);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(170, 310, 70, 70))
        self.button_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 0, 0)")
        self.button_3.setObjectName("button_3")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(250, 230, 70, 70))
        self.button_plus.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(8, 8, 8)")
        self.button_plus.setObjectName("button_plus")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(10, 230, 70, 70))
        self.button_4.setStyleSheet("color:rgb(9, 9, 9);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(90, 230, 70, 70))
        self.button_5.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(4, 4, 4)")
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(170, 230, 70, 70))
        self.button_6.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(9,9,9)")
        self.button_6.setObjectName("button_6")
        self.button_subsctraction = QtWidgets.QPushButton(self.centralwidget)
        self.button_subsctraction.setGeometry(QtCore.QRect(250, 150, 70, 70))
        self.button_subsctraction.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(9, 9, 9)")
        self.button_subsctraction.setObjectName("button_subsctraction")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(90, 150, 70, 70))
        self.button_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(8, 8, 8)")
        self.button_8.setObjectName("button_8")
        self.button_clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_all.setGeometry(QtCore.QRect(90, 70, 70, 70))
        self.button_clear_all.setStyleSheet("color:rgb(85, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon.fromTheme("calculatortrashbutton.png")
        self.button_clear_all.setIcon(icon)
        self.button_clear_all.setObjectName("button_clear_all")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(10, 150, 70, 70))
        self.button_7.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 0, 0)")
        self.button_7.setObjectName("button_7")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(170, 150, 70, 70))
        self.button_9.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(7, 7, 7)")
        self.button_9.setObjectName("button_9")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(10, 70, 70, 70))
        self.button_clear.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 170, 127)")
        self.button_clear.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_clear.setIcon(icon)
        self.button_clear.setFlat(False)
        self.button_clear.setObjectName("button_clear")
        self.button_multiple = QtWidgets.QPushButton(self.centralwidget)
        self.button_multiple.setGeometry(QtCore.QRect(250, 70, 70, 70))
        self.button_multiple.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(11, 11, 11)")
        self.button_multiple.setObjectName("button_multiple")
        self.button_division = QtWidgets.QPushButton(self.centralwidget)
        self.button_division.setGeometry(QtCore.QRect(170, 70, 70, 70))
        self.button_division.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.button_division.setObjectName("button_division")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(10, 390, 70, 70))
        self.button_0.setStyleSheet("color:rgb(15, 15, 15);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.button_0.setObjectName("button_0")
        self.button_fraction = QtWidgets.QPushButton(self.centralwidget)
        self.button_fraction.setGeometry(QtCore.QRect(250, 310, 70, 70))
        self.button_fraction.setStyleSheet("color:rgb(4, 4, 4);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.button_fraction.setObjectName("button_fraction")
        self.button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.button_equal.setGeometry(QtCore.QRect(250, 390, 70, 70))
        self.button_equal.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(7, 7, 7)")
        self.button_equal.setObjectName("button_equal")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(10, 20, 301, 31))
        self.label_result.setAutoFillBackground(False)
        self.label_result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_result.setObjectName("label_result")
        self.label_operation = QtWidgets.QLabel(self.centralwidget)
        self.label_operation.setGeometry(QtCore.QRect(10, 0, 301, 31))
        self.label_operation.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_operation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_operation.setObjectName("label_operation")
        self.button_parenthesis_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_parenthesis_1.setGeometry(QtCore.QRect(90 , 390 , 70 , 70))
        self.button_parenthesis_1.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(7, 7, 7)")
        self.button_parenthesis_1.setObjectName("button_equal_2")
        self.button_parenthesis_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_parenthesis_2.setGeometry(QtCore.QRect(170 , 390 , 70 , 70))
        self.button_parenthesis_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(7, 7, 7)")
        self.button_parenthesis_2.setObjectName("button_equal_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 331, 51))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.button_1.raise_()
        self.button_2.raise_()
        self.button_3.raise_()
        self.button_plus.raise_()
        self.button_4.raise_()
        self.button_5.raise_()
        self.button_6.raise_()
        self.button_subsctraction.raise_()
        self.button_8.raise_()
        self.button_clear_all.raise_()
        self.button_7.raise_()
        self.button_9.raise_()
        self.button_clear.raise_()
        self.button_multiple.raise_()
        self.button_division.raise_()
        self.button_0.raise_()
        self.button_fraction.raise_()
        self.button_equal.raise_()
        self.label_result.raise_()
        self.label_operation.raise_()
        self.button_parenthesis_1.raise_( )
        self.button_parenthesis_2.raise_( )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 328, 21))
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
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_subsctraction.setText(_translate("MainWindow", "-"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_clear_all.setText(_translate("MainWindow", "clear \n"
" all"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_multiple.setText(_translate("MainWindow", "x"))
        self.button_division.setText(_translate("MainWindow", "÷"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_fraction.setText(_translate("MainWindow", "."))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.label_result.setText(_translate("MainWindow", ""))
        self.label_operation.setText(_translate("MainWindow", ""))
        self.button_parenthesis_1.setText(_translate("MainWindow" , "("))
        self.button_parenthesis_2.setText(_translate("MainWindow" , ")"))
	    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
