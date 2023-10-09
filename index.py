from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import sys
import os
from os import path
ui,_ = loadUiType('main.ui')

Result = 0
num1 = 0
num2 = 0
Result_str =' '

class MainApp(QMainWindow , ui):
    
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Buttons()
        self.Exit_func()
    
    
    def Handle_UI (self):
        self.setWindowTitle('Calculator')  
        self.setFixedSize(533,253)
    
    def Handle_Buttons(self):
        self.Add.clicked.connect(self.Add_func)
        self.Sub.clicked.connect(self.Sub_func)
        self.Div.clicked.connect(self.Div_func)
        self.Mul.clicked.connect(self.Mul_func)
        

    
    def Handle_Inputs (self):
        global Result,num1,num2
        num1_str=self.Number1.text()
        num2_str=self.Number2.text()
        num1 = int(num1_str)
        num2 = int(num2_str)
 
    
    def Handle_Output (self):
        global Result ,Result_str
        Result_str = str(Result)
        self.ResultBox.setText(Result_str)
        #self.Resultlabel.setText(Result_str)
    
    def Add_func (self):
        global Result,num1,num2
        self.Handle_Inputs()
        Result=num1+num2      
        self.Handle_Output()
        print(Result_str)
        print(Result)

    
    def Sub_func (self):
        global Result,num1,num2
        self.Handle_Inputs()
        Result=num1-num2
        self.Handle_Output()
        print(Result)
        print(Result_str)


           
     
    
    def Mul_func (self):
        global Result,num1,num2
        self.Handle_Inputs()
        Result=num1*num2
        self.Handle_Output()
        print(Result_str)
        print(Result)
      
  
    
    def Div_func (self):
        global Result,num1,num2
        self.Handle_Inputs()
        if num2 == 0:
            QMessageBox.warning(self, "Dividing Falied", "Please Set Number2 by value not equal Zero")
            return
        else :
            Result=num1/num2
            self.Handle_Output()
            print(Result)
            print(Result_str)

                     
    
    def Exit_func (self):
        self.actionExit.triggered.connect(exit)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()