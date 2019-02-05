#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:55:18 2019

@author: KrySt
"""
from random import randint
from tkinter import *
vysledek=0  
class App(): 
    
    def __init__(self, master):
        
        #vytvoření okna
        self.frame = Frame(master)
        self.frame.pack()
            
        #vytvoření nápisu operace
        self.Label = Label(self.frame, text=u"Vyber jakou operaci chceš provést:")
        self.Label.grid(row = 0, column=0,columnspan=10)
        
        #button na ukončení
        self.button = Button(self.frame,text="Konec",command=master.destroy)
        self.button.grid(row = 5,column=0,columnspan=2)
        
        #okno na zadání čísla
        self.number1entry=Entry(self.frame,width=4)
        self.number1entry.grid(row=1,column=0)
        
        self.number2entry=Entry(self.frame,width=4)
        self.number2entry.grid(row=1,column=5)
        
        self.Label = Label(self.frame, text=u"=")
        self.Label.grid(row = 2, column=0,columnspan=1)
        
        self.vysledek=Entry(self.frame,width=4)
        self.vysledek.grid(row=2,column=1)
        
        self.tlacitko = Button(self.frame,width=4, text=u"Vypočítej")
        self.tlacitko.grid(row=2, column= 3)
        self.radiobuttons()
        
    def radiobuttons(self):
        
        #vybrat plus
        self.var = IntVar()
        self.plus = Radiobutton(self.frame, text="+",command=self.plus,variable= self.var,value=1)
        self.plus.grid(row=1,column=1,columnspan=1)
        
        #vybrat minus
        self.minus = Radiobutton(self.frame, text="-",command=self.minus,variable= self.var,value=2)
        self.minus.grid(row=1,column=2,columnspan=1)
        
        #vybrat násobení
        self.times = Radiobutton(self.frame, text="*",command=self.times,variable= self.var,value=3)
        self.times.grid(row=1,column=3,columnspan=1)
        
        #vybrat dělení
        self.div = Radiobutton(self.frame, text="/",command=self.div,variable= self.var,value=4)
        self.div.grid(row=1,column=4,columnspan=1)
    

        #funkce plus, která se vybere radiobuttonem plus a provede se
    def plus(self):
        #náhodné číslo od 1-99
        self.number1 = randint(1,99)
        #nejdřív první okno smaže obsah
        self.number1entry.delete(0,5)
        #poté do něho vloží výše generované číslo
        self.number1entry.insert(0,str(self.number1))
        #to stejny, ale generuje od prvního čísla do 100, aby nebylo nižší
        self.number2 = randint(self.number1,100)
        #zase smaže a vloží vygenerované číslo
        self.number2entry.delete(0,5)
        self.number2entry.insert(0,str(self.number2))
        #vytvořím proměnnou result, která obsahuje správnou odpověď
        self.result = self.number1 + self.number2
        return()
    
    def minus(self):
        self.number1 = randint(1,99)
        self.number1entry.delete(0,5)
        self.number1entry.insert(0,str(self.number1))
        self.number2 = randint(0, self.number1)
        self.number2entry.delete(0,5)
        self.number2entry.insert(0,str(self.number2))
        self.result = self.number1 - self.number2
        return()
        
    def times(self):
        self.number1 = randint(1,9)
        self.number1entry.delete(0,5)
        self.number1entry.insert(0,str(self.number1))
        self.number2 = randint(1,9)
        self.number2entry.delete(0,5)
        self.number2entry.insert(0,str(self.number2))
        self.result = self.number1 * self.number2
        return()
        
    
    def div(self):
        self.number1 = randint(2,100)
        self.number1entry.delete(0,5)
        self.number1entry.insert(0,str(self.number1))
        self.number2 = randint(2,10) 
        self.number2entry.delete(0,5)
        self.number2entry.insert(0,str(self.number2))
        self.result = self.number1 * self.number2
        return()
        




root = Tk()
app = App(root)
root.mainloop()
        



