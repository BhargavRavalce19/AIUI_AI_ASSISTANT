from AiUi import Ui_MainWindow
from PyQt5 import QtCore, QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QApplication
import sys

class MainThread(QThread): 
    
    def __init__(self):
        super(MainThread,self).__init__()
        
startExe = MainThread()     
    
class Gui_Start(QtWidgets.QMainWindow):
     
    def __init__(self):
         super().__init__()
         
         self.gui = Ui_MainWindow()
         self.gui.setupUi(self)
         
         self.gui.pb_start.clicked.connect(self.startTask)
         self.gui.pb_exit.clicked.connect(self.close)
         
    def startTask(self):
        
        self.gui.l1 = QtGui.QMovie("GIF//83ec7dae7e76751eecca2adcf0dcfc49.gif")
        self.gui.gif_1.setMovie(self.gui.l1)
        self.gui.l1.start()
        
        self.gui.l2 = QtGui.QMovie("deco//3ab74962b138cb7396156fd96d0f6408.gif")
        self.gui.gif_2.setMovie(self.gui.l2)
        self.gui.l2.start()
        
        self.gui.l3 = QtGui.QMovie("deco//Untitled design (2).gif")
        self.gui.gif_3.setMovie(self.gui.l3)
        self.gui.l3.start()
        
        self.gui.l4 = QtGui.QMovie("deco//01.gif")
        self.gui.gif_4.setMovie(self.gui.l4)
        self.gui.l4.start()
        
        self.gui.l5 = QtGui.QMovie("deco//01.gif")
        self.gui.gif_5.setMovie(self.gui.l5)
        self.gui.l5.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()
        
        startExe.start()
        
    def showTimeLive(self):
        time1=QTime.currentTime()
        time=time1.toString()
        date1=QDate.currentDate()
        date=date1.toString()
        label_t=time
        label_d=date
        
        self.gui.tb_time.setText(label_t)
        self.gui.tb_date.setText(label_d)
        
        
GuiApp=QApplication(sys.argv)
cAiUi = Gui_Start()
cAiUi.show()
exit(GuiApp.exec_()) 