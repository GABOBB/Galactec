from tkinter import *
from User_Profile import User
import User_Profile as UP
import tkinter as tk
import JsonManager as JM
import v_ayuda as VA
import pygame
import sys
import os


class login_wndw(tk.Tk):
    
    def __init__(self, wndw):
        super().__init__()
        self.title("Log In")
        self.geometry('250x300')
        self.resizable(width=NO,height=NO)

        self.wndw_back = wndw
        
        self.canvas = tk.Canvas(self, bg="black", width=250, height=300)
        self.canvas.pack()
        
        self.MSSG = Label(self.canvas,text="",bg='Black',fg='red')
        self.MSSG.place(x=15,y=10)
        
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

        self.HELP_B = Button(self.canvas, text='HELP', bg='green1', fg='black', command=lambda: VA.v_help(self))
        self.HELP_B.place(x=200, y=20)
        
        self.protocol("WM_DELETE_WINDOW", self.exit)
        
        self.mainloop()
        
    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')
        
    def try_logIn(self,U,P):
        
        U = U.strip()
        P = P.strip()
        if(len(U)>>0 and len(P)>>0):  
            J = Verify_credencials(U,P)
            if(J.U_IN != None):
                self.destroy()
                self.wndw_back.confirmed(J.U_IN)
                self.wndw_back.deiconify()
            else:
                self.MSSG.config(text="Usuario o contraseña incorrecta")
                self.canvas.update()         
        elif(len(U)<=0 or len(P)<=0):
            self.MSSG.config(text="Credenciales incompletas")
            self.canvas.update()

    def Sing_Up(self):
        self.withdraw()
        SU.singup_wndw(self)

class Verify_credencials():
    def __init__(self,User,Psswdr):
        self.List_user = None
        self.U_IN = None
        self.L_U = self.load_users()
        self.verify(User,Psswdr)
        
    def load_users(self):
        L = JM.JSONManager('usuarios.json').cargar_lista(User)
        for l in L:
            print(l.get_NMBR())
        return L
        
    def verify(self, User, Psswdr):
        for U in self.L_U:
            print(U.get_NMBR() + '-----' + User +";"+U.get_PSSWRD()+'-----'+ Psswdr)
            if(U.get_NMBR() == User and U.get_PSSWRD() == Psswdr):
                self.U_IN = U
                return 0
            else:
                self.U_IN = None

