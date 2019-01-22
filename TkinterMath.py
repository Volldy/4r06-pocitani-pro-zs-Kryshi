#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:55:18 2019

@author: KrySt
"""
from random import randint
from tkinter import *
  
class App(): 
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        
        self.Label = Label(frame, text=u"Operace: ")
        self.Label.grid(row = 0, column=0,columnspan=3)
    
        self.button = Button(frame,text="Konec",command=master.destroy)
        self.button.grid(row = 5,column=0,columnspan=2)
        
        self.var = IntVar()
        self.plus = Radiobutton(frame, text="+",variable= self.var,value=1)
        self.plus.grid(row=0,column=3,columnspan=1)
        
        self.minus = Radiobutton(frame, text="-",variable= self.var,value=2)
        self.minus.grid(row=0,column=4,columnspan=1)
        
        self.times = Radiobutton(frame, text="*",variable= self.var,value=3)
        self.times.grid(row=0,column=5,columnspan=1)
        
        self.div = Radiobutton(frame, text="/",variable= self.var,value=4)
        self.div.grid(row=0,column=6,columnspan=1)
        
        self.cislo1=Entry(frame,width=4)
        self.cislo1.grid(row=1,column=0)
        
        #self.lblOperace=Label(frame,text = self.var)
        
        
        
        
    def plus(self, x, y):
        self.x = randint(1,99)
        self.y = randint(0,100 -x)
        self.result = x + y
        return()
    
    def minus(self):
        self.x = randint(1,99)
        self.y = randint(0, self.x)
        self.result = self.x - self.y
        
    def times(self):
        self.x = randint(1,9)
        self.y = randint(1,9)
        self.result = self.x * self.y
        
    def div(self):
        self.result = randint(1,9)
        self.y = randint(1,9)
        self.x = self.result * self.y
        
    #def vypocet(self)
        
        
        


if __name__=="__main__":

    root = Tk()
    app = App(root)
    root.mainloop()
        



