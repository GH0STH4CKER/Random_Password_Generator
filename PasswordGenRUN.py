from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets as qt
from PyQt5 import QtGui as gui
from PyQt5 import QtCore
from PasswordGenUI import Ui_Dialog as ui
import sys,re,string,random

class Window(qt.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()


        self.ui = ui()
        self.ui.setupUi(self) # Initalize UI

        self.oldPos = self.pos()
        self.ui.btnGenerate.move(self.ui.btnGenerate.x()+80,self.ui.btnGenerate.y())
        for group in qt.QMainWindow.parentWidget().findChildren(QWidget):
            print(group)

        # Connect ButtonPress event to functions
        self.ui.btnGenerate.clicked.connect(self.passGen)
        self.ui.btncopy.clicked.connect(self.copyToCLipboard)
        self.ui.btnMin.clicked.connect(self.minimizeApp)
        self.ui.btnMax.clicked.connect(self.maximizeApp)
        self.ui.btnClose.clicked.connect(self.closeApp)

        # MouseHover event for minimize,maximize,close buttons
        self.ui.btnMin.installEventFilter(self)
        self.ui.btnMax.installEventFilter(self)
        self.ui.btnClose.installEventFilter(self)

        self.ui.txtPass.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.txtPass.setDisabled(True) # Disable password field
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # Remove default titlebar

    # Random Password Generating function
    def passGen(self) : 

        global characters,Upper,Lower,Nums,Symbol
        Upper,Lower,Nums,Symbol = False,False,False,False

        if self.ui.checkUppercase.isChecked() and  self.ui.checkLowercase.isChecked() and self.ui.checkNumbers.isChecked() and self.ui.checkSymbols.isChecked() :
            Upper,Lower,Nums,Symbol = True,True,True,True
            divi = 4
            characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()")
            
        elif self.ui.checkUppercase.isChecked() and  self.ui.checkLowercase.isChecked() and self.ui.checkNumbers.isChecked() :
            Upper,Lower,Nums = True,True,True
            divi = 3
            characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
            
        elif self.ui.checkUppercase.isChecked() and  self.ui.checkLowercase.isChecked() and self.ui.checkSymbols.isChecked() :
            Upper,Lower,Symbol = True,True,True
            divi = 3
            characters = list(string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()")
            
        elif self.ui.checkLowercase.isChecked() and  self.ui.checkSymbols.isChecked() and self.ui.checkNumbers.isChecked() :
            Lower,Nums,Symbol = True,True,True
            divi = 3
            characters = list(string.ascii_lowercase + string.digits + "!@#$%^&*()")
            
        elif self.ui.checkUppercase.isChecked() and  self.ui.checkSymbols.isChecked() and self.ui.checkNumbers.isChecked() :
            Upper,Nums,Symbol = True,True,True
            divi = 3
            characters = list(string.ascii_uppercase + string.digits + "!@#$%^&*()")
            
        elif self.ui.checkUppercase.isChecked() and self.ui.checkLowercase.isChecked() :
            Upper,Lower = True,True
            divi = 2
            characters = list(string.ascii_lowercase + string.ascii_uppercase)
            
        elif self.ui.checkSymbols.isChecked() and self.ui.checkNumbers.isChecked() :
            Nums,Symbol = True,True
            divi = 2
            characters = list(string.digits + "!@#$%^&*()")
            
        elif self.ui.checkSymbols.isChecked() and self.ui.checkLowercase.isChecked() :
            Lower,Symbol = True,True
            divi = 2
            characters = list(string.ascii_lowercase + "!@#$%^&*()")
            
        elif self.ui.checkUppercase.isChecked() and self.ui.checkNumbers.isChecked() :
            Upper,Nums = True,True
            divi = 2
            characters = list(string.ascii_uppercase + string.digits)
            
        elif self.ui.checkSymbols.isChecked() and self.ui.checkUppercase.isChecked() :
            Upper,Symbol = True,True
            divi = 2
            characters = list(string.ascii_uppercase + "!@#$%^&*()")
            
        elif self.ui.checkLowercase.isChecked() and self.ui.checkNumbers.isChecked() :
            Lower,Nums = True,True
            divi = 2
            characters = list(string.ascii_lowercase + string.digits)
            
        elif self.ui.checkUppercase.isChecked() :
            Upper = True
            divi = 1
            characters = list(string.ascii_uppercase)
            
        elif self.ui.checkLowercase.isChecked() :
            Lower = True
            divi = 1
            characters = list(string.ascii_lowercase)
            
        elif self.ui.checkNumbers.isChecked() :
            Nums = True
            divi = 1
            characters = list(string.digits)
            
        elif self.ui.checkSymbols.isChecked() :
            Symbol = True
            divi = 1
            characters = list("!@#$%^&*()")
        else :
            msg1 = qt.QMessageBox()
            msg1.setIcon(qt.QMessageBox.Warning)
            msg1.setText("At least one checkbox must be selected !")
            msg1.setWindowTitle("Checkbox Not Selected")
            msg1.setStandardButtons(qt.QMessageBox.Ok)
            msg1.exec_()  


        alphabet_lower = list(string.ascii_lowercase)
        alphabet_upper = list(string.ascii_uppercase)
        digits = list(string.digits)
        special_characters = list("!@#$%^&*()")
       
        length = self.ui.Pass_length.value() 

        password = []
        characters_count = 0

        if Lower == True :
            lowercase_count = random.randint(1,length//divi)  
            for i in range(lowercase_count):
                password.append(random.choice(alphabet_lower))
            characters_count += lowercase_count

        if Upper == True :        
            uppercase_count = random.randint(1,length//divi) 
            for i in range(uppercase_count):
                password.append(random.choice(alphabet_upper))
            characters_count += uppercase_count

        if Nums == True :
            digits_count = random.randint(1,length//divi) 
            for i in range(digits_count):
                password.append(random.choice(digits))
            characters_count += digits_count

        if Symbol == True :
            special_characters_count = random.randint(1,length//divi) 
            for i in range(special_characters_count):
                password.append(random.choice(special_characters))
            characters_count += special_characters_count

        if characters_count < length:
            random.shuffle(characters)
            for i in range(length - characters_count):
                password.append(random.choice(characters))

        random.shuffle(password)
        
        self.ui.txtPass.setText("".join(password))
    # function for copy btton
    def copyToCLipboard(self) :

        import clipboard
        copytext = self.ui.txtPass.text()
        if len(copytext) > 0 :
            clipboard.copy(copytext)
    # minimize button functionality
    def minimizeApp(self) :
        self.showMinimized()
    # maximize button functionality
    def maximizeApp(self) :
        if self.isMaximized() :
            self.showNormal()
            #self.ui.btnMax.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Downloads/maximize4.png);background-color: transparent;")
        else :
            self.showMaximized()
            #self.ui.btnMax.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Downloads/restore.png);background-color: transparent;")
    # close button functionality  
    def closeApp(self) :
        self.close()   

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # MouseHover Event > change button images
    def eventFilter(self, object, event):
        
        if event.type() == QEvent.Enter and object is self.ui.btnMin :
            self.ui.btnMin.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Desktop/Python_projects/ICO/minimize_highlight.png);background-color: transparent;")
            return True
        elif event.type() == QEvent.Leave and object is self.ui.btnMin :
            self.ui.btnMin.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Desktop/Python_projects/ICO/minimize_normal.png);background-color: transparent;")
        
        if event.type() == QEvent.Enter and object is self.ui.btnMax :
            self.ui.btnMax.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Desktop/Python_projects/ICO/maximize_highlight.png);background-color: transparent;")
            return True
        elif event.type() == QEvent.Leave and object is self.ui.btnMax :
            self.ui.btnMax.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Desktop/Python_projects/ICO/maximize_normal.png);background-color: transparent;")

        if event.type() == QEvent.Enter and object is self.ui.btnClose :
            self.ui.btnClose.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Desktop/Python_projects/ICO/close_highlight.png);background-color: transparent;")
            return True
        elif event.type() == QEvent.Leave and object is self.ui.btnClose :
            self.ui.btnClose.setStyleSheet("background-image: url(C:/Users/Dimuth De Zoysa/Desktop/Python_projects/ICO/close_normal.png);background-color: transparent;")
        
        return False

# Run Application
app = qt.QApplication([])
application = Window()
application.show()
app.exec()