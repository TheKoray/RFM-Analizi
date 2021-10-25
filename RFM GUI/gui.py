# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:38:51 2021

@author: koray
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from Customer_Komp import Customer_Komp
from Customer_Enjek import Customer_Enjek
from Customer_Kap import Customer_Kap
from Customer_Balata import Customer_Balata

#Customer_Komp Modülünü çağırıyoruz.Komprasör için Müşteri Segmentlerini buradan alacağız.
ky = Customer_Komp() 

#Customer_Enjek modülünü çağırıyoruz.Enjektör için Müşteri Segmentlerini buradan alacağız.
ky_enjek = Customer_Enjek() 

#Customer_Kap modülünü çağırıyoruz.Komprasör Kapağı için Müşteri Segmentlerini buradan alacağız.
ky_kapak = Customer_Kap() 

#Customer_Balata modülünü çağırıyoruz.Komprasör Kapağı için Müşteri Segmentlerini buradan alacağız.
ky_balata = Customer_Balata()

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.pencere()
        
    def pencere(self):
        
        #Pencere
        self.setGeometry(500,500,650,650)
        self.setWindowTitle("Müsteri Segmentasyonu")
        
        #Background Resim
        self.label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('araba.jpg.jpg')
        self.label.setPixmap(self.pixmap)        
        
        #Champions buton
        self.champ_buton = QtWidgets.QPushButton(self)
        self.champ_buton.setText("Champions")
        self.champ_buton.move(90,100)
        
        #Sleep Buton
        self.sleep_buton = QtWidgets.QPushButton(self)
        self.sleep_buton.setText("Sleep")
        self.sleep_buton.move(270,100)
        
        #Risk Buton
        self.risk_buton = QtWidgets.QPushButton(self)
        self.risk_buton.setText('Risk')
        self.risk_buton.move(450,100)
        
        #New Buton 
        self.new_buton = QtWidgets.QPushButton(self)
        self.new_buton.setText("New")
        self.new_buton.move(90,150)
        
        #Promising Buton
        self.pro_buton = QtWidgets.QPushButton(self)
        self.pro_buton.setText('Promising')
        self.pro_buton.move(270,150)
        
        #Attention Buton
        self.att_buton = QtWidgets.QPushButton(self)
        self.att_buton.setText("Attention")
        self.att_buton.move(450,150)
        
        #Temizle Butonu
        self.clear_buton = QtWidgets.QPushButton(self)
        self.clear_buton.setText('Clear')
        self.clear_buton.move(270,230)
        
        #RadioButton Komprasör
        self.radio_komp = QtWidgets.QRadioButton(self)
        self.radio_komp.setText('Komprasör')
        self.radio_komp.move(90,50)
            
        #RadioButton Enjektör
        self.radio_enjek = QtWidgets.QRadioButton(self)
        self.radio_enjek.setText('Enjektör')
        self.radio_enjek.move(220,50)
        
        #RadioButton K.Kapağı
        self.radio_kapak = QtWidgets.QRadioButton(self)
        self.radio_kapak.setText('K.Kapağı')
        self.radio_kapak.move(350,50)
        
        #RadioButton Balata
        self.radio_bal = QtWidgets.QRadioButton(self)
        self.radio_bal.setText('Balata')
        self.radio_bal.move(480,50)
           
        #result
        self.result = QtWidgets.QTextEdit(self)
 
        self.result.setGeometry(350,520,520,350)
        self.result.setGeometry
        self.result.move(70,280) 
        
        self.show()
        
        self.clear_buton.clicked.connect(self.clear_tikla)
              
        #self.radio_komp.clicked.connect(self.komp_tikla)
        #self.radio_enjek.clicked.connect(self.enjek_tikla)
        
        self.champ_buton.clicked.connect(self.champ_tikla)
        self.sleep_buton.clicked.connect(self.sleep_tikla)
        self.risk_buton.clicked.connect(self.risk_tikla)
        self.new_buton.clicked.connect(self.new_tikla)
        self.pro_buton.clicked.connect(self.pro_tikla)
        self.att_buton.clicked.connect(self.attention_tikla)
        
#%% CHAMPIONS

    def champ_tikla(self): #Champions PushButtonu için Fonskiyon
        
        if self.radio_komp.isChecked(): #Komprasör RadioButtonu True olursa
            
            count = 1
            
            self.result.append("KOMPRASÖR - CHAMPIONS") #Çıktı alanımıza ekleme
            self.result.append("-" * 97)
            
            for i in ky.Champions(): #Komprasör Müşterilerinden Champions Segmentinde olanları alırız
                
                self.result.append(str(count) + " - " + str(i)) #Çıktı alanımıza Müşterileri eklme
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
                
        if self.radio_enjek.isChecked(): #Enjektör RadioButtonu True olursa
            
            count  = 1
            
            self.result.append("ENJEKTÖR - CHAMPIONS")
            self.result.append("-" * 97)
            
            
            for i in ky_enjek.Champions(): #Enjektör Müşterilerinden Champions Segmentinde olanları alırız
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
        
        if self.radio_kapak.isChecked(): #K.Kapağı RadioButtonu True olursa
        
            self.result.append("KOMP. KAPAĞI - CHAMPIONS")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_kapak.Champions(): #K. Kapağı Müşterilerinden Champions Segmentinde olanları alırız
                
                self.result.append(str(count) + " - " + str(i))
                count +=1  
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
        
        if self.radio_bal.isChecked(): #Balata RadioButtonu True olursa
        
            self.result.append("BALATA - CHAMPIONS")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_balata.Champions():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1      
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
#%% SLEEP  
     
    def sleep_tikla(self):
        
        if self.radio_komp.isChecked():
            
  
           self.result.append("KOMPRASÖR - SLEEP")
           self.result.append("-" * 97)
           
           count = 1
           
           for i in ky.Sleep():               
               
              self.result.append(str(count) + " - " + str(i))
              count +=1
           
           self.result.append("-" * 97)
           self.result.append(str(count - 1) + " tane Müşteri Vardır")
        
        if self.radio_enjek.isChecked():
            
            self.result.append("ENJEKTÖR - SLEEP")
            self.result.append("-" * 97)

            count = 1
            for i in ky_enjek.Sleep():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
        
        if self.radio_kapak.isChecked():
            
            self.result.append("KOMP. KAPAĞI - SLEEP")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_kapak.Sleep():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
            
        if self.radio_bal.isChecked():
            
            self.result.append("BALATA - SLEEP")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_balata.Sleep():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")

#%% RISK
              
    def risk_tikla(self):
        
        if self.radio_komp.isChecked():
            
            self.result.append("KOMPRASÖR - RISK")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky.Risk():
                
                self.result.append(str(count) + " - " + str(i))
                
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
                
        if self.radio_enjek.isChecked():
            
            self.result.append("ENJEKTÖR - RISK")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky_enjek.Risk():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
        
        if self.radio_kapak.isChecked():
            
            self.result.append("KOMP. KAPAĞI - RISK")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky_kapak.Risk():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
            
        if self.radio_bal.isChecked():
            
            self.result.append("BALATA - RISK")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_balata.Risk():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Var")

#%% NEW CUSTOMERS    
            
    def new_tikla(self):
        
        if self.radio_komp.isChecked():
            
            self.result.append("KOMPRASÖR - NEW CUSTOMER")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky.New():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Var")
        
        if self.radio_enjek.isChecked():
            
            self.result.append("ENJEKTÖR - NEW CUSTOMER")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky_enjek.New():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Var")
                
        if self.radio_kapak.isChecked():
            
            self.result.append("KOMP. KAPAĞI - NEW CUSTOMER")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky_kapak.New():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)    
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
            
        if self.radio_bal.isChecked():
            
            self.result.append("BALATA - NEW CUSTOMER")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_balata.New():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Var")
 
#%% PROMISING            
 
    def pro_tikla(self):
        
        if self.radio_komp.isChecked():
            
            self.result.append("KOMPRASÖR - PROMISING")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky.Promising():
            
               self.result.append(str(count) + " - " + str(i))
            
               count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
               
        if self.radio_enjek.isChecked():
            
            self.result.append("ENJEKTÖR - PROMISING")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky_enjek.Promising():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
                
        if self.radio_kapak.isChecked():
            
            self.result.append("KOMP. KAPAĞI - PROMISING")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky_kapak.Promising():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
            
        if self.radio_bal.isChecked():
            
            self.result.append("BALATA - PROMISING")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_balata.Promising():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")

#%% ATTENTION

    def attention_tikla(self):
        
        if self.radio_komp.isChecked():
            
            self.result.append("KOMPRASÖR - ATTENTION")
            self.result.append("-" * 97)
            
            count = 1
        
            for i in ky.Attention():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
            
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
                
        if self.radio_enjek.isChecked():
            
            self.result.append("ENJEKTÖR - ATTENTION")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_enjek.Attention():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
                
        if self.radio_kapak.isChecked():
            
            self.result.append("KOMP. KAPAĞI - ATTENTION")
            self.result.append("-" * 97)
            
            count = 1
            for i in ky_kapak.Attention():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
            
        if self.radio_bal.isChecked():
            
            self.result.append("BALATA - ATTENTION")
            self.result.append("-" * 97)
            
            count = 1
            
            for i in ky_balata.Attention():
                
                self.result.append(str(count) + " - " + str(i))
                count +=1
                
            self.result.append("-" * 97)
            self.result.append(str(count - 1) + " tane Müşteri Vardır")
         
    def clear_tikla(self):
        
        self.result.clear()
        

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
        
        