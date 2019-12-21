import sys

from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import QClipboard

from ui.calc import Ui_MainWindow


class Calculator(QtWidgets.QMainWindow):
    def __init__ (self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_operator = False
        self.number1 = None
        self.number2 = None
        self.operator = None
        self.is_parenthesis = False
        self.parenthesis_1 = None
        self.parenthesis_2 = None
        
    def keyPressEvent (self , event):
        key = event.key()
        
        print(key)
        
        if key == QtCore.Qt.Key_0:
            self.make_key_button_click(button=self.ui.button_0)
        elif key == QtCore.Qt.Key_1:
            self.make_key_button_click(button=self.ui.button_1)
        elif key == QtCore.Qt.Key_2:
            self.make_key_button_click (button=self.ui.button_2)
        elif key == QtCore.Qt.Key_3 :
            self.make_key_button_click (button=self.ui.button_3)
        elif key == QtCore.Qt.Key_4:
            self.make_key_button_click(button=self.ui.button_4)
        elif key == QtCore.Qt.Key_5 :
            self.make_key_button_click(button=self.ui.button_5)
        elif key == QtCore.Qt.Key_6 :
            self.make_key_button_click(button=self.ui.button_6)
        elif key == QtCore.Qt.Key_7 :
            self.make_key_button_click(button=self.ui.button_7)
        elif key == QtCore.Qt.Key_8 :
            self.make_key_button_click(button=self.ui.button_8)
        elif key == QtCore.Qt.Key_9 :
            self.make_key_button_click(button=self.ui.button_9)
        elif key == QtCore.Qt.Key_Plus:
            self.make_key_operator_click(button=self.ui.button_plus)
        elif key == QtCore.Qt.Key_Minus:
            self.make_key_operator_click (self.ui.button_subsctraction)
        elif key == QtCore.Qt.Key_Asterisk:
            self.make_key_operator_click (self.ui.button_multiple)
        elif key == QtCore.Qt.Key_Slash:
            self.make_key_operator_click (self.ui.button_division)
        elif key == QtCore.Qt.Key_Backspace:
            self.button_back()
        elif key == QtCore.Qt.Key_Delete:
            self.clear_all()
        elif key == 46:
            self.set_fraction()
        elif key == 40:
            self.make_key_parenthesis_button(button=self.ui.button_parenthesis_1)
        elif key == 41:
            self.make_key_parenthesis_button(button=self.ui.button_parenthesis_2)

    def make_button_click (self , button) :
        def button_click() :
            self.ui.label_operation.setText (self.ui.label_operation.text() + button.text())
            label_content = self.ui.label_operation.text()
            if self.operator is not None :
                self.update_operation (label_content)
            self.is_operator = False
        
        return button_click

    def make_key_button_click (self , button) :
        def button_click() :
            self.ui.label_operation.setText (self.ui.label_operation.text() + button.text())
            label_content = self.ui.label_operation.text()
            if self.operator is not None :
                self.update_operation (label_content)
            self.is_operator = False
    
        return button_click()
    
    def update_operation (self , content) :
        print(self.is_parenthesis)
        if len (content) > 1 and not self.is_parenthesis:
            content = content.replace ("x" , "*")
            content = content.replace ("÷" , "/")
            try :
                result = eval (content)
            except ZeroDivisionError :
                result = "Err"
            if result is None :
                self.ui.label_result.setText ("Err")
            else :
                self.ui.label_result.setText (str (result))
    
    def set_fraction (self) :
        label_content = self.ui.label_operation.text()
        if not self.is_operator and len (label_content) != 0 :
            self.ui.label_operation.setText (label_content + self.ui.button_fraction.text())
    
    def make_operator_click (self , button) :
        def set_operator() :
            label_content = self.ui.label_operation.text()
            if not self.is_operator and len (label_content) != 0 :
                self.ui.label_operation.setText (label_content + button.text())
                self.is_operator = True
                self.operator = button.text()
        
        return set_operator

    def make_key_operator_click (self , button) :
        def set_operator() :
            label_content = self.ui.label_operation.text()
            if not self.is_operator and len (label_content) != 0 :
                self.ui.label_operation.setText (label_content + button.text())
                self.is_operator = True
                self.operator = button.text()
    
        return set_operator()
    
    def equals_button (self) :
        if self.ui.label_result.text() == "Err" :
            self.ui.label_result.clear()
        self.ui.label_operation.setText (self.ui.label_result.text())
        self.ui.label_result.clear()
    
    def clear_all (self) :
        self.ui.label_operation.clear()
        self.ui.label_result.clear()
        self.operator = None

    def is__operator (self, char) :
        if char != "+" and char != "-" and char != "x" and char != "÷" :
            return False
        else :
            return True
    
    def button_back (self) :
        self.ui.label_operation.setText (self.ui.label_operation.text() [ :-1 ])
        last_char = self.ui.label_operation.text() [ -1 : ]
        print ("last char:", last_char)
        
        if not self.is__operator (last_char) :
            label_content = self.ui.label_operation.text()
            self.update_operation (label_content)
        else :
            self.is_operator = True
            self.ui.label_result.clear()
        
        if last_char == '' :
            self.ui.label_result.clear()
    
    def make_parenthesis_button(self, button):
        
        def parenthesis_button():
            label_content = self.ui.label_operation.text ( )
            button_content = button.text ( )
            if button_content == "(":
                print("operator", self.is_operator)
                if not self.is_parenthesis:
                    if not self.is_operator:
                        self.ui.label_operation.setText(label_content + "x" + button_content)
                    else:
                        self.ui.label_operation.setText(label_content + button_content)
                    self.is_parenthesis = True
            elif button_content == ")":
                if self.is_parenthesis:
                    self.ui.label_operation.setText (label_content + button_content)
                    self.is_parenthesis = False
                    self.update_operation(label_content + button_content)
                    
        return parenthesis_button

    def make_key_parenthesis_button (self , button) :
    
        def parenthesis_button ( ) :
            label_content = self.ui.label_operation.text ( )
            button_content = button.text ( )
            if button_content == "(" :
                print ("operator" , self.is_operator)
                if not self.is_parenthesis :
                    if not self.is_operator :
                        self.ui.label_operation.setText (label_content + "x" + button_content)
                    else :
                        self.ui.label_operation.setText (label_content + button_content)
                    self.is_parenthesis = True
            elif button_content == ")" :
                if self.is_parenthesis :
                    self.ui.label_operation.setText (label_content + button_content)
                    self.is_parenthesis = False
                    self.update_operation (label_content + button_content)
    
        return parenthesis_button()

		
     
    
    def is__parenthesis (operation) :
        if operation != "(" and operation != ")" :
            return False
        else :
            return True

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Calculator()
    
    ui = MainWindow.ui

    ui.button_0.clicked.connect (MainWindow.make_button_click (button=ui.button_0))
    ui.button_1.clicked.connect (MainWindow.make_button_click (button=ui.button_1))
    ui.button_2.clicked.connect (MainWindow.make_button_click (button=ui.button_2))
    ui.button_3.clicked.connect (MainWindow.make_button_click (button=ui.button_3))
    ui.button_4.clicked.connect (MainWindow.make_button_click (button=ui.button_4))
    ui.button_5.clicked.connect (MainWindow.make_button_click (button=ui.button_5))
    ui.button_6.clicked.connect (MainWindow.make_button_click (button=ui.button_6))
    ui.button_7.clicked.connect (MainWindow.make_button_click (button=ui.button_7))
    ui.button_8.clicked.connect (MainWindow.make_button_click (button=ui.button_8))
    ui.button_9.clicked.connect (MainWindow.make_button_click (button=ui.button_9))
    ui.button_plus.clicked.connect (MainWindow.make_operator_click (button=ui.button_plus))
    ui.button_subsctraction.clicked.connect (MainWindow.make_operator_click (button=ui.button_subsctraction))
    ui.button_multiple.clicked.connect (MainWindow.make_operator_click (button=ui.button_multiple))
    ui.button_division.clicked.connect (MainWindow.make_operator_click (button=ui.button_division))
    ui.button_fraction.clicked.connect (MainWindow.set_fraction)
    ui.button_clear_all.clicked.connect (MainWindow.clear_all)
    ui.button_clear.clicked.connect (MainWindow.button_back)
    ui.button_equal.clicked.connect (MainWindow.equals_button)
    ui.button_parenthesis_1.clicked.connect(MainWindow.make_parenthesis_button(button=ui.button_parenthesis_1))
    ui.button_parenthesis_2.clicked.connect(MainWindow.make_parenthesis_button(button=ui.button_parenthesis_2))
    
    MainWindow.show()
    sys.exit(app.exec_())