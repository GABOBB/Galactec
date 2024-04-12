from tkinter import *
import tkinter as tk
import pygame
import sys
import os

class login:

    def __init__(self,C_A):
        self.canvas=None
        self.load()
        self.C_A = C_A
        
        

    
    
    def begin(self,X,y):
        print(X,y)
        # se verificarian las credenciales
    
    def get_C(self):
        return self.canvas
    
    def exit(self):
        self.canvas.destroy
        #self.canvas = self.C_A
    

    def load(self):
       
        self.canvas = tk.Canvas( bg="black", width=250, height=300)
        self.canvas.pack()
        
        
        
        UserL=Label(self.canvas, text='Username:',bg='green2',fg='Black')
        UserL.place(x=15,y=50)

        UserE=Entry(self.canvas,bg='black',fg='green2')
        UserE.place(x=10,y=90)

        Pwrdl=Label(self.canvas, text='Password:',bg='green1',fg='black')
        Pwrdl.place(x=10,y=140)

        PwrdE=Entry(self.canvas,bg='black',fg='green2')
        PwrdE.place(x=10,y=180)

        LoginB = Button(self.canvas, text= 'LogIn',bg='green1',fg='black',command=lambda: self.begin(UserE.get(),PwrdE.get()))
        LoginB.place(x=20,y=240)
        
        cancel = Button(self.canvas,text='Exit',bg='green1',command=lambda: self.exit())
        cancel.place(x=80,y=240)