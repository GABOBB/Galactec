from tkinter import *
from User_Profile import User
import User_Profile as UP
import tkinter as tk
import JsonManager as JM
import CorreoManager as CM
import pygame
import sys
import os


class singup_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Sing Up")
        self.geometry('250x500')
        self.resizable(width=NO, height=NO)

        self.wndw_back = wndw

        self.canvas = tk.Canvas(self, bg="black", width=250, height=500)
        self.canvas.pack()

        self.MSSG = Label(self.canvas, text="", bg='Black', fg='red')
        self.MSSG.place(x=10, y=10)

        NameL = Label(self.canvas, text='Real name:', bg='green2', fg='Black')
        NameL.place(x=10, y=50)

        NameE = Entry(self.canvas, bg='black', fg='green2')
        NameE.place(x=10, y=90)

        UserL = Label(self.canvas, text='Username:', bg='green2', fg='Black')
        UserL.place(x=10, y=140)

        UserE = Entry(self.canvas, bg='black', fg='green2')
        UserE.place(x=10, y=180)

        EmailL = Label(self.canvas, text='Email:', bg='green2', fg='Black')
        EmailL.place(x=10, y=230)

        EmailE = Entry(self.canvas, bg='black', fg='green2')
        EmailE.place(x=10, y=270)

        Pwrdl = Label(self.canvas, text='Password:', bg='green1', fg='black')
        Pwrdl.place(x=10, y=320)

        PwrdE = Entry(self.canvas, bg='black', fg='green2')
        PwrdE.place(x=10, y=360)

        SingUpB = Button(self.canvas, text='SingUp', bg='green1', fg='black',
                         command=lambda: self.sign_up(email=EmailE.get(), user=UserE.get(), real_name=NameE.get(),
                                                      password=PwrdE.get()))
        SingUpB.place(x=20, y=410)

        ExitB = Button(self.canvas, text='Exit', bg='green1', command=lambda: self.exit())
        ExitB.place(x=80, y=410)

        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')

    def sign_up(self, email, user, real_name, password):
        correo_manager = CM.CorreoManager(usuario="mendezariaspablo@gmail.com", password="zswt frhf gewi xzfu")

        email = email.strip()
        user = user.strip()
        real_name = real_name.strip()
        password = password.strip()

        if len(email) >> 0 and len(user) >> 0 and len(real_name) >> 0 and len(password) >> 0:
            U = UP.User(real_name, user, password, email, None, None, None)
            jm = JM.JSONManager('usuarios.json')
            L = jm.cargar_lista(User)
            Check = True
            for l in L:
                print(l.get_USR() +'---'+ user)
                if(l.get_USR() == user):
                    Check = False
                    break
                    
            if(Check):
                if correo_manager.verificar_correo(email):
                    self.destroy()
                    
                    print(len(L))
                    L += [U]
                    print(len(L))
                    jm.guardar_lista(L) 
                    self.wndw_back.deiconify()

                else:
                    self.MSSG.config(text="Correo inválido")
                    self.canvas.update()
            else:
                self.MSSG.config(text="Usuario inválido")
                self.canvas.update()
        else:
            self.MSSG.config(text="Credenciales incompletas")
            self.canvas.update()

        correo_manager.cerrar_sesion()
