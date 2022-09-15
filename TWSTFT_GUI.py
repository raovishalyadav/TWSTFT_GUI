'''
Copyright (C) 2019 Vishal Yadav
'''
import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
import easygui
import sys
import socket
import datetime
import os
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import math
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtCore, QtGui
import random
import easygui
import sys
import socket
import os
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import math
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtCore, QtGui

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 590, 200, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(1000, 510, 200, 70))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1000, 680, 200, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1000, 770, 200, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1000, 860, 200, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton1.setStyleSheet('font: 14pt Roboto;background: black;;color: red;border-style: solid;border-width: 0px;border-radius: 0px;border-color: black ;')
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(5, 510, 230, 30))
        self.pushButton5.setObjectName("pushButton")
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(250, 510, 230, 30))
        self.pushButton6.setObjectName("pushButton")
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(495, 510, 230, 30))
        self.pushButton7.setObjectName("pushButton")
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.setGeometry(QtCore.QRect(740, 510, 230, 30))
        self.pushButton8.setObjectName("pushButton")


        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton9.setGeometry(QtCore.QRect(3, 0, 1204, 500))
        self.pushButton9.setObjectName("pushButton")
        self.pushButton9.setStyleSheet('font: 36pt Roboto;background: black;;color: red;border-style: solid;border-width: 0px;border-radius: 0px;border-color: black ;')

        self.pushButton.setStyleSheet("font: 25pt Roboto;background: black;color: green;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black green black green;")
        self.pushButton_2.setStyleSheet('font: 25pt Roboto;background: black;;color: red;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black red black red;')
        self.pushButton_3.setStyleSheet("font: 25pt Roboto;background: black;color: rgb(255,223,0);border-style: solid;border-width: 10px;border-radius: 0px;border-color: black rgb(255,223,0) black rgb(255,223,0);")
        self.pushButton_4.setStyleSheet("font: 25pt Roboto;background: black;color: blue;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black blue black blue;")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.graphicsView.setGeometry(QtCore.QRect(3, 0, 1204, 500))
        self.graphicsView.setBackgroundBrush(QColor("black"))
        labelStyle = {'color': 'red', 'font-size': '14pt'}

        self.graphicsView.setLabel('left','Time difference ( ns )', **labelStyle)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle("TWSTFT NPLI - ISRO")
        self.pushButton.setText(_translate("MainWindow", "REAL-TIME"))
        self.pushButton1.setText(_translate("MainWindow", "STD. DEV."))
        self.pushButton_2.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_3.setText(_translate("MainWindow", "LOCK %"))
        self.pushButton_4.setText(_translate("MainWindow", "DATA"))
        self.pushButton5.setText(_translate("MainWindow", "TSA-UTC (NPLI)"))
        self.pushButton6.setText(_translate("MainWindow", "TSC-UTC (NPLI)"))
        self.pushButton7.setText(_translate("MainWindow", "TSB-UTC (NPLI)"))
        self.pushButton8.setText(_translate("MainWindow", "TSD-UTC (NPLI)"))
        self.pushButton9.setText(_translate("MainWindow", "TSD-UTC (NPLI)"))


        self.pushButton.pressed.connect(self.Real_Time)
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_3.clicked.connect(self.Lock)
        self.pushButton_4.clicked.connect(self.Raw_Data)

        self.pushButton.setToolTip('To Start Plotting the Graph')
        self.pushButton_2.setToolTip('To Clear the Graph')
        self.pushButton_3.setToolTip('To Pause the Graph')

    def show_about_dialog(self):
        text = "<center>" \
               "<h1>TWSTFT NPLI - ISRO</h1>" \
               "&#8291;" \
               "<img src=icon_exit.png>" \
               "</center>" \
               "<p>Version 1.0<br/>" \
               "Copyright  &copy; 2019 Vishal Yadav, Md. Aslam</p>"
        QMessageBox.about(self, "About GUI", text)

    def Real_Time(self):

        self.s = socket.socket()
        self.s.connect((ip,port))
        self.a =[]
        self.b =[]
        self.c =[]
        self.c1 =[]
        self.c2 =[]
        self.c3 =[]
        values = []
        self.del_data = []
        for line9 in enumerate(open("terminal_del.txt", "r")):
           self.del_data.append(line9)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(0)
        self.pushButton.setStyleSheet("font: 25pt Roboto;background: green;border-style: solid;border-width: 10px;border-radius: 10px;border-color: light green;")
        self.pushButton_2.setStyleSheet('font: 25pt Roboto;background: black;;color: red;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black red black red;')
        self.pushButton_3.setStyleSheet("font: 25pt Roboto;background: black;color: rgb(255,223,0);border-style: solid;border-width: 10px;border-radius: 0px;border-color: black rgb(255,223,0) black rgb(255,223,0);")
        self.pushButton_4.setStyleSheet("font: 25pt Roboto;background: black;color: blue;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black blue black blue;")
        self.pushButton_4.setEnabled(False)
        self.graphicsView.clear()


    def updater(self):
        _translate = QtCore.QCoreApplication.translate
        self.graphicsView.clear()
        msg = "!SYS:DDP;OCD=1\n"
        msg1 = "!SYS:DDP;ORT=1\n"
        self.s.sendto(msg.encode(),(ip,port))
        self.s.sendto(msg1.encode(),(ip,port))
        data = self.s.recv(1024)
        data_comp = data.decode()



        values = []

        for i,line in enumerate(data_comp.splitlines(),1):
           if ( ("%Rx1>" in line) and (len(line) > 150) ) :
              self.graphicsView.setGeometry(QtCore.QRect(3, 0, 1204, 500))
              if (float(line[19:21]) in range(0,10)):
                 if (len(line[140:149])>2) and (line[140:149].strip() != "0.000"):

                    self.a.append(line[16:18]+":"+line[19:21]+":"+line[22:24])
                    self.b.append(float(line[140:149])-float(self.del_data[27][1]))

                    values.append(self.a[-1])
                    values.append(self.b[-1])
                 if len(self.b)>14400:
                    del self.b[0]
                    del self.a[0]

              if (float(line[19:21]) in range(10,20)):
                 if (len(line[140:149])>2) and (line[140:149].strip() != "0.000"):

                    self.a.append(line[16:18]+":"+line[19:21]+":"+line[22:24])
                    self.b.append(float(line[140:149])-float(self.del_data[83][1]))

                    values.append(self.a[-1])
                    values.append(self.b[-1])
                 if len(self.b)>14400:
                    del self.b[0]
                    del self.a[0]


              if (float(line[19:21]) in range(30,40)):

                 if (len(line[140:149])>2) and (line[140:149].strip() != "0.000"):

                    self.a.append(line[16:18]+":"+line[19:21]+":"+line[22:24])
                    self.b.append(float(line[140:149])-float(self.del_data[55][1]))

                    values.append(self.a[-1])
                    values.append(self.b[-1])
                 if len(self.b)>14400:
                    del self.b[0]
                    del self.a[0]


              if (float(line[19:21]) in range(40,50)):
                 if (len(line[140:149])>2) and (line[140:149].strip() != "0.000"):

                    self.a.append(line[16:18]+":"+line[19:21]+":"+line[22:24])
                    self.b.append(float(line[140:149])-float(self.del_data[111][1]))

                    values.append(self.a[-1])
                    values.append(self.b[-1])

                 if len(self.b)>14400:
                    del self.b[0]
                    del self.a[0]

              labelStyle = {'color': 'red', 'font-size': '14pt'}
              if ( float(line[19:21]) in range(0,10) ) and ( len(values)>0 ):
                 self.graphicsView.setLabel('bottom','TSA-UTC (NPLI)', **labelStyle)
                 self.model.insertRow(0)
                 self.model.setData(self.model.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
                 self.model.setData(self.model.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
                 for q in range(2):
                    self.model.setData(self.model.index(0, q), values[q])
                 self.model.removeRow(14400)
                 self.show()
                 if ( (line[140:149] != "0.000") ):
                    if(  (float(line[16:18]) == 23.0) and (float(line[19:21]) in range(59,61))  ):
                       self.c = []
                    self.c.append(float(line[140:149])+999.56)
                    mean = sum(self.c) / len(self.c)   # mean
                    var  = sum(pow(x-mean,2) for x in self.c) / len(self.c)  # variance
                    std  = math.sqrt(var)
                    self.pushButton1.setText(_translate("MainWindow", "STD. DEV. = "+str(round((std),4))))

              if ( float(line[19:21]) in range(10,20) ) and ( len(values)>0 ):

                 self.graphicsView.setLabel('bottom','TSC-UTC (NPLI)', **labelStyle)
                 self.model1.insertRow(0)
                 self.model1.setData(self.model1.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
                 self.model1.setData(self.model1.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
                 for q in range(2):
                    self.model1.setData(self.model1.index(0, q), values[q])
                 self.model1.removeRow(14400)
                 self.show()
                 if ( (line[140:149] != "0.000") ):
                    if(  (float(line[16:18]) == 23.0) and (float(line[19:21]) in range(59,61))  ):
                       self.c1 = []
                    self.c1.append(float(line[140:149])+float(self.del_data[55][1].replace('\n','')))#
                    mean = sum(self.c1) / len(self.c1)   # mean
                    var  = sum(pow(x-mean,2) for x in self.c1) / len(self.c1)  # variance
                    std  = math.sqrt(var)
                    self.pushButton1.setText(_translate("MainWindow", "STD. DEV. = "+str(round((std),4))))



                 self.graphicsView.setLabel('bottom','TSA-TSC', **labelStyle)


              if ( float(line[19:21]) in range(30,40) ) and ( len(values)>0 ):
                 self.graphicsView.setLabel('bottom','TSB-UTC (NPLI)', **labelStyle)#banglore
                 self.model2.insertRow(0)
                 self.model2.setData(self.model2.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
                 self.model2.setData(self.model2.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)

                 for q in range(2):
                    self.model2.setData(self.model2.index(0, q), values[q])
                 self.model2.removeRow(14400)
                 self.show()
                 if ( (line[140:149] != "0.000")): 
                    if(  (float(line[16:18]) == 23.0) and (float(line[19:21]) in range(59,61))  ):
                       self.c2 = []
                    self.c2.append(float(line[140:149])+float(self.del_data[83][1].replace('\n','')))
                    mean = sum(self.c2) / len(self.c2)   # mean
                    var  = sum(pow(x-mean,2) for x in self.c2) / len(self.c2)  # variance
                    std  = math.sqrt(var)
                    self.pushButton1.setText(_translate("MainWindow", "STD. DEV. = "+str(round((std),4))))

              if ( float(line[19:21]) in range(40,50) ) and ( len(values)>0 ):
                 self.graphicsView.setLabel('bottom','TSD-UTC (NPLI)', **labelStyle)
                 self.model3.insertRow(0)
                 self.model3.setData(self.model3.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
                 self.model3.setData(self.model3.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
                 for q in range(2):
                    self.model3.setData(self.model3.index(0, q), values[q])
                 self.model3.removeRow(14400)
                 self.show()
                 if ( (line[140:149] != "0.000") ):
                    if(  (float(line[16:18]) == 23.0) and (float(line[19:21]) in range(59,61))  ):
                       self.c3 = []
                    self.c3.append(float(line[140:149])+float(self.del_data[111][1].replace('\n','')))
                    mean = sum(self.c3) / len(self.c3)   # mean
                    var  = sum(pow(x-mean,2) for x in self.c3) / len(self.c3)  # variance
                    std  = math.sqrt(var)
                    self.pushButton1.setText(_translate("MainWindow", "STD. DEV. = "+str(round((std),4))))

              if( not((float(line[19:21]) in range(20,30)) or (float(line[19:21]) in range(50,60))) ):

                 self.graphicsView.clear()

           xdict = dict(enumerate(self.a))
           string = self.graphicsView.getAxis('bottom')
           string.setTicks([xdict.items()])

           self.graphicsView.plot(list(xdict.keys()),self.b, pen='r',symbol='x', symbolPen='w', symbolSize=8)#symbol- d t h o p s x  color-c d b g k l m rw y

           if  ( (("%Rx1>" in line) and (len(line) > 50) and (int(line[22:24]) in range(0,60))) and ( ((int(line[19:21]) in range(20,30)))  or  (int(line[19:21]) in range(50,60))) ):
              self.graphicsView.setGeometry(QtCore.QRect(0, 0, 0, 0))
              if  (9-int(line[20:21])) >= 1:
                 self.pushButton9.setText(_translate("MainWindow", " UNUSED DATA SLOT !!! \n\nWill be back in %d minutes and %d seconds"%( (9-int(line[20:21])) ,(59-int(line[22:24])))))
              elif (9-int(line[20:21])) < 1:
                 self.pushButton9.setText(_translate("MainWindow", " UNUSED DATA SLOT !!! \n\nWill be back in %d seconds"%(59-int(line[22:24]))))
              elif ((9-int(line[20:21])) == 0) and ((59-int(line[22:24])) == 0):
                 self.graphicsView.setGeometry(QtCore.QRect(3, 0, 1204, 500))

    def stop(self,MainWindow):
        self.graphicsView.setGeometry(QtCore.QRect(3, 0, 1204, 500))

        self.model.deleteLater()
        self.model = QStandardItemModel(self)
        self.table.setModel(self.model)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setStyleSheet("background: black;color: white;")
        self.model.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])
        self.model1.deleteLater()
        self.model1 = QStandardItemModel(self)
        self.table1.setModel(self.model1)
        self.table1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table1.setStyleSheet("background: black;color: white;")
        self.model1.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])
        self.model2.deleteLater()
        self.model2 = QStandardItemModel(self)
        self.table2.setModel(self.model2)
        self.table2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table2.setStyleSheet("background: black;color: white;")
        self.model2.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])
        self.model3.deleteLater()
        self.model3 = QStandardItemModel(self)
        self.table3.setModel(self.model3)
        self.table3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table3.setStyleSheet("background: black;color: white;")
        self.model3.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])

        self.graphicsView.clear()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.pushButton.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_2.setStyleSheet("font: 25pt Roboto;background: red;border-style: solid;border-width: 10px;border-radius: 10px;border-color: light red;")
        self.pushButton.setStyleSheet("font: 25pt Roboto;background: black;color: green;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black green black green;")
        self.pushButton_3.setStyleSheet("font: 25pt Roboto;background: black;color: rgb(255,223,0);border-style: solid;border-width: 10px;border-radius: 0px;border-color: black rgb(255,223,0) black rgb(255,223,0);")
        self.pushButton_4.setStyleSheet("font: 25pt Roboto;background: black;color: blue;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black blue black blue;")

    def Lock(self):

        self.p = 0
        self.q = 0
        self.s = 0
        self.t = 0

        filename = easygui.fileopenbox( default=r"/usr/TWSTFT_DATA/*", filetypes= "*.txt")
        if (os.path.getsize(filename)/1024)!=0:
           f = open(filename,"r")
           for pos, line in enumerate(f.readlines()):
              if float(line[14:16]) in range(0,10):
                 self.p = self.p + 1
              if float(line[14:16]) in range(10,20):
                 self.q = self.q + 1
              if float(line[14:16]) in range(30,40):
                 self.s = self.s + 1
              if float(line[14:16]) in range(40,50):
                 self.t = self.t + 1

           msg = QMessageBox()
           msg.setStyleSheet("background-color: rgb(0, 123, 0);")
           msg.question(self, 'LOCKED PERCENTAGE  ', " 00-09 : "+str('%.2f' %((self.p)/144))+' %'+'\n'+" 10-19 : "+str('%.2f' %((self.q)/144))+' %'+'\n'" 30-39 : "+str('%.2f' %((self.s)/144))+' %'+'\n'" 40-49 : "+str('%.2f' %((self.t)/144))+' %'+'\n' , QMessageBox.Ok)
           msg.setText('to select click "show details"')
           msg.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
           msg.setDetailedText('line 1\nline 2\nline 3')
        else:
           QMessageBox.question(self, 'ERROR MESSAGE ', " NO DATA !!! ", QMessageBox.Close)

        self.pushButton_3.setStyleSheet("font: 25pt Roboto;background: yellow;border-style: solid;border-width: 10px;border-radius: 10px;border-color: light yellow;")
        self.pushButton.setStyleSheet("font: 25pt Roboto;background: black;color: green;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black green black green;")
        self.pushButton_2.setStyleSheet('font: 25pt Roboto;background: black;;color: red;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black red black red;')

        self.pushButton_4.setStyleSheet("font: 25pt Roboto;background: black;color: blue;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black blue black blue;")

    def Raw_Data(self, MainWindow):
      _translate = QtCore.QCoreApplication.translate

      labelStyle = {'color': 'white', 'font-size': '14pt'}
      self.graphicsView.setLabel('bottom','', **labelStyle)
      filename = easygui.fileopenbox(filetypes= "*.txt",multiple = True)#/usr/TWSTFT_DATA
      if len(filename) > 0:
         msgBox = QtGui.QMessageBox()
         msgBox.setText('Please Select the Time-Slot')
         correctBtn = msgBox.addButton('00-09', QtGui.QMessageBox.YesRole)
         incorrectBtn = msgBox.addButton('10-19', QtGui.QMessageBox.YesRole)
         cancelBtn = msgBox.addButton('30-39', QtGui.QMessageBox.YesRole)
         Btn = msgBox.addButton('40-49', QtGui.QMessageBox.YesRole)
         msgBox.exec_()

      if msgBox.clickedButton() == correctBtn:
          lower = 0
          upper = 10
      elif msgBox.clickedButton() == incorrectBtn:
          lower = 10
          upper = 20
      elif msgBox.clickedButton() == cancelBtn:
          lower = 30
          upper = 40
      elif msgBox.clickedButton() == Btn:
          lower = 40
          upper = 50

      x = []
      y = []
      z = []
      for selected_file in range(0,len(filename)):
         f = open(filename[selected_file],'r')
         for pos, line in enumerate(f.readlines()):
             if (float(line[25:]) != 0) and ( int(line[14:16]) in  range(lower,upper) ):

                y.append(float(line[25:]))
                x.append(line[8:19].replace('_',' '))
                z.append(line[0:10].replace('_',' ').replace(' ','/'))

      if len(y) <1:
         QMessageBox.about(self, "ERROR !!!", 'NO DATA FOUND !!!')

      self.model.setData(self.model.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
      self.model.setData(self.model.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
      self.model1.setData(self.model1.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
      self.model1.setData(self.model1.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
      self.model2.setData(self.model2.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
      self.model2.setData(self.model2.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
      self.model3.setData(self.model3.index(0, 1), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)
      self.model3.setData(self.model3.index(0, 0), QtCore.QVariant(QtCore.Qt.AlignCenter),QtCore.Qt.TextAlignmentRole)

      for row in range(1,len(x)+1):
         if lower== 0 and upper == 10:
            self.model.insertRow(row-1)
            self.model.setData(self.model.index(row-1, 0), '('+str(x[row-1][0:2])+') '+str(x[row-1][3:]).replace(' ',':'))
            self.model.setData(self.model.index(row-1, 1), y[row-1])

         if lower== 10 and upper == 20:
            self.model1.insertRow(row-1)
            self.model1.setData(self.model1.index(row-1, 0), x[row-1])
            self.model1.setData(self.model1.index(row-1, 1), y[row-1])
         if lower== 30 and upper == 40:
            self.model2.insertRow(row-1)
            self.model2.setData(self.model2.index(row-1, 0), x[row-1])
            self.model2.setData(self.model2.index(row-1, 1), y[row-1])
         if lower== 40 and upper == 50:
            self.model3.insertRow(row-1)
            self.model3.setData(self.model3.index(row-1, 0), x[row-1])
            self.model3.setData(self.model3.index(row-1, 1), y[row-1])



      mean = sum(y) / len(y)   # mean
      var  = sum(pow(x-mean,2) for x in y) / len(y)  # variance
      std  = math.sqrt(var)
      self.pushButton1.setText(_translate("MainWindow", "STD. DEV. = "+str(round((std),4))))

      xdict = dict(enumerate(x))
      string = self.graphicsView.getAxis('bottom')
      string.setTicks([xdict.items()])
      self.pushButton_4.setStyleSheet("font: 25pt Roboto;background: blue;border-style: solid;border-width: 10px;border-radius: 10px;border-color: light blue;")
      self.graphicsView.plot(list(xdict.keys()),y, pen='r',symbol='x', symbolPen='w', symbolSize=8)#symbol- d t h o p s x  color-c d b g k l m r w y
      self.pushButton.setStyleSheet("font: 25pt Roboto;background: black;color: green;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black green black green;")
      self.pushButton_2.setStyleSheet('font: 25pt Roboto;background: black;;color: red;border-style: solid;border-width: 10px;border-radius: 0px;border-color: black red black red;')
      self.pushButton_3.setStyleSheet("font: 25pt Roboto;background: black;color: rgb(255,223,0);border-style: solid;border-width: 10px;border-radius: 0px;border-color: black rgb(255,223,0) black rgb(255,223,0);")
      self.pushButton.setEnabled(False)
      labelStyle = {'color': 'red', 'font-size': '14pt'}
      self.graphicsView.setLabel('bottom',str(z[0])+'-'+str(z[-1]), **labelStyle)

    def menu_color(self):
        selected_color = QColorDialog.getColor()
        self.mainMenu.setStyleSheet("QWidget { background: %s;color: black;border-style: outset;border-width: 1px;border-radius:1px ;border-color: black}" % selected_color.name())

class TimerMessageBox(QtGui.QMessageBox):
    def __init__(self,mins=0, secs=0, parent=None):
        super(TimerMessageBox, self).__init__(parent)
        self.setWindowTitle("wait")
        self.time_to_wait = mins
        self.time_wait = secs
        self.setText("        UNUSED DATA SLOT !!! \n\nWill be back in %d minutes and %d seconds"%(self.time_to_wait,self.time_wait))
        self.setStandardButtons(QtGui.QMessageBox.NoButton)
        '''self.timer = QtCore.QTimer(self)
        self.timer.setIrandom.randrange(20, 50, 3)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()'''

    def changeContent(self):
        if self.time_to_wait != 0 and self.time_wait == 0:
           self.time_to_wait -= 1
           if self.time_to_wait < 0:
              self.time_to_wait = 59

        self.time_wait -= 1
        if self.time_to_wait != 0 and self.time_wait < 0:
           self.time_wait = 59

        self.setText("        UNUSED DATA SLOT !!! \n\nWill be back in %d minutes and %d seconds"%(self.time_to_wait,self.time_wait))
        if self.time_to_wait == 0 and self.time_wait == 0:
           self.timer.stop()
           self.close()

    def closeEvent(self, event):
        self.timer.stop()

class Delay(QWidget):

    def __init__(self, parent):
        super(Delay, self).__init__()
        self.setFixedSize(800,800)
        Delay.setStyleSheet(self,"background-color: white")
        self.setWindowTitle("TERMINAL DELAYS")
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        font = QFont()
        font.setBold(True)
        txt_dat = 0
        tab_data = ['TSA - NPLI','TSB - NPLI','TSC - NPLI','TSD - NPLI']
        lbl_data = ['ISTRAC SATRE Modem to SAW Filter ','ISTRAC SAW Filter','ISTRAC SAW Filter to UP Converter ','ISTRAC SSPA ','ISTRAC UP Converter + ISTRAC UP Converter to SSPA + NPLI LNA to Down Converter + NPLI Down_converter','ISTRAC Up Sagnac ','NPLI Down Sagnac ','NPLI LNA','NPLI Down Converter to SAW Filter','NPLI SAW Filter','NPLI Saw Filter to Satre Modem','NPLI SATRE Modem To SAW Filter ','NPLI SAW Filter','NPLI SAW Filter to UP Converter ','NPLI SSPA','NPLI UP Converter + NPLI UP Converter to SSPA + ISTRAC LNA To Down Converter + ISTRAC Down Converter','NPLI Up Sagnac ','ISTRAC Down Sagnac ','ISTRAC LNA','ISTRAC Down Converter to SAW Filter ','ISTRAC SAW Filter','ISTRAC Saw to SATRE Modem','1PPS Generation Point To SATRE Modem 1 PPS IN ','SATRE Modem 1PPS IN to 1PPS Strobe ','(NPLI) PPS to PPS Distributor ','(NPLI) PPS Distributor to SATRE Modem IN','(NPLI) SATRE Modem 1PPS IN to 1PPS Strobe ']
        f_read = open("terminal_del.txt", "r")
        lines = f_read.readlines()
        self.line_edit0 = {}
        self.btn2 = {}

        for tab_data_con in range(1,5):
            self.tab1 = QWidget()
            self.tabs.addTab(self.tab1,str(tab_data[tab_data_con-1]))
            self.tab1.layout = QFormLayout()
            self.tab1.setLayout(self.tab1.layout)

            for lbl in range(1,28):
                label = QtGui.QLabel(str(lbl_data[lbl-1]))
                label.setAlignment(QtCore.Qt.AlignLeft)
                label.setFont(font)
                self.line_edit0[txt_dat] = QLineEdit(lines[txt_dat])
                var.append(float(self.line_edit0[txt_dat].text().replace('\n','')))
                self.tab1.layout.addWidget(self.line_edit0[txt_dat])
                self.tab1.layout.addRow(label, self.line_edit0[txt_dat])
                txt_dat = txt_dat +1

            self.submit = QPushButton("SUBMIT")
            self.submit.setStyleSheet("font: 15pt Roboto;height: 62px; width: 600px;border-width: 10px;background: black;color: red;border-color: black red black red")
            self.tab1.layout.addRow(self.submit)
            self.btn1 = QPushButton("CURRENT TERMINAL DELAY = ")
            self.btn1.setStyleSheet("font: 15pt Roboto;height: 62px; width: 600px;border-width: 10px;background: black;color: red;border-color: black red black red")
            self.btn2[tab_data_con-1] = QPushButton(lines[txt_dat])
            var.append(lines[txt_dat].replace('\n',''))
            txt_dat = txt_dat +1
            self.btn2[tab_data_con-1].setStyleSheet("font: 15pt Roboto;height: 62px; width: 600px;border-width: 10px;background: black;color: red;border-color: black red black red")
            self.tab1.layout.addRow(self.btn1,self.btn2[tab_data_con-1])
            self.btn1.setEnabled(False)
            self.btn2[tab_data_con-1].setEnabled(False)
            self.layout.addWidget(self.tabs)
            self.submit.clicked.connect(self.button_click)
        f_read.close()

    def button_click(self):
        var1 = []
        var2 = []
        try:
            for file100 in range(1,112):
                if(file100%28==0):
                    continue
                var1.append(float(self.line_edit0[file100-1].text()))
        except Exception as e:
            pass

        try:
            for str_val in range(0,4):
                sum1 = sum(var1[(str_val*27)+0:(str_val*27)+11])
                sum2 = sum(var1[(str_val*27)+11:(str_val*27)+22])
                sum3 = sum(var1[(str_val*27)+22:(str_val*27)+24])
                sum4 = sum(var1[(str_val*27)+24:(str_val*27)+27])

                Net_Round_Trip_Delay = (sum1-sum2)/2
                Net_1PPS_Delay = sum3-sum4
                Final_Offset_Value = round((Net_Round_Trip_Delay + Net_1PPS_Delay),3)
                var2.append(Final_Offset_Value)
                self.btn2[str_val].setText(str(Final_Offset_Value))

        except Exception as e:
            pass

        var1 = var1[:27] + [var2[0]] + var1[27:]
        var1 = var1[:55] + [var2[1]] + var1[55:]
        var1 = var1[:83] + [var2[2]] + var1[83:]
        var1 = var1[:111] + [var2[3]] + var1[111:]

        f_final = open("terminal_del.txt","w")

        for put_data in range(1,113):
            f_final.write(str(var1[put_data-1])+"\n")

        f_final.close()

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow,QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.mainMenu=self.menuBar()
        self.mainMenu.setStyleSheet("background: black;color: red;border-style: solid;border-width: 1px;border-radius:0px ;border-color: red")

        self.editMenu=self.mainMenu.addMenu('&Help')
        about_action = QAction(QIcon('photo.png'),"About", self)
        self.editMenu.addAction(about_action)
        about_action.triggered.connect(self.show_about_dialog)

        self.exit=self.mainMenu.addMenu('&Exit')
        some1 = QAction(QIcon('delete.png'),"Exit GUI", self)
        self.exit.addAction(some1)
        some1.triggered.connect(qApp.quit)

        self.delay = self.mainMenu.addMenu('&Delay-Parameters')
        edit = QAction("edit-parameters", self)
        self.delay.addAction(edit)
        edit.triggered.connect(self.show_window2)
        self.setupUi(self)

        self.table = QTableView(self)
        self.table.setGeometry(5, 567, 230, 400)
        self.model = QStandardItemModel(self)
        self.table.setModel(self.model)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setStyleSheet("background: black;color: white;")
        self.model.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])

        self.table1 = QTableView(self)
        self.table1.setGeometry(250, 567, 230, 400)
        self.model1 = QStandardItemModel(self)
        self.table1.setModel(self.model1)
        self.table1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table1.setStyleSheet("background: black;color: white;")
        self.model1.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])

        self.table2 = QTableView(self)
        self.table2.setGeometry(495, 567, 230, 400)
        self.model2 = QStandardItemModel(self)
        self.table2.setModel(self.model2)
        self.table2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table2.setStyleSheet("background: black;color: white;")
        self.model2.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])

        self.table3 = QTableView(self)
        self.table3.setGeometry(740, 567, 230, 400)
        self.model3 = QStandardItemModel(self)
        self.table3.setModel(self.model3)
        self.table3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table3.setStyleSheet("background: black;color: white;")
        self.model3.setHorizontalHeaderLabels(['TIMESTAMP','OFFSET'])

        self.Delay = Delay(self)

    def show_window2(self):
        self.Delay.show()

if __name__ == "__main__":
    ip = "192.168.20.27"
    port = 2000
    lower = 0
    upper = 10
    found  = []
    found1 = []
    filename = []
    x = []
    y = []
    a = []
    b = []
    var = []
    var1 = []
    var2 = []
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QMainWindow{background-color: #333333;background-repeat: no-repeat;background-position: center;border: 1px solid red;}")
    w = MyWindow()
    w.showMaximized()
    sys.exit(app.exec_())
