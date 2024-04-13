from tkinter import *
import tkinter as tk
import pygame
import sys
import os


class login_wndw(tk.Tk):
    
    def __init__(self, wndw):
        super().__init__()
        self.title("Log In")
        self.geometry('250x300')
        self.title('Log In')
        self.resizable(width=NO,height=NO)
        
        self.wndw_back = wndw
        
        self.canvas = tk.Canvas(self, bg="black", width=250, height=300)
        self.canvas.pack()
        
        UserL=Label(self.canvas, text='Username:',bg='green2',fg='Black')
        UserL.place(x=15,y=50)

        UserE=Entry(self.canvas,bg='black',fg='green2')
        UserE.place(x=10,y=90)

        Pwrdl=Label(self.canvas, text='Password:',bg='green1',fg='black')
        Pwrdl.place(x=10,y=140)

        PwrdE=Entry(self.canvas,bg='black',fg='green2')
        PwrdE.place(x=10,y=180)

        LoginB = Button(self.canvas, text= 'LogIn',bg='green1',fg='black',command=lambda: self.try_logIn(UserE.get(),PwrdE.get()))
        LoginB.place(x=20,y=240)
        
        cancel = Button(self.canvas,text='Exit',bg='green1',command=lambda: self.exit())
        cancel.place(x=80,y=240)
        
        Rgstr = Button(self.canvas, text='Dont have an account yet?',bg='black',fg='green1',bd=0, command=lambda: self.Sing_Up())
        Rgstr.place(x=10,y=200)
        
        self.mainloop()
        
    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')
        
    def try_logIn(self,U,P):
        print('Log In' + ' -> ' + U + ',' +  P)
    
    def Sing_Up(self):
        print('sing_Up')

#login_wndw()
