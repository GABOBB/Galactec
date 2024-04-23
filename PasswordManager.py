from tkinter import *
from User_Profile import User
import User_Profile as UP
import tkinter as tk
import JsonManager as JM
import CorreoManager as CM
import random
import pygame
import sys
import os


class recover_password_wndw(tk.Tk):
    def __init__(self, code, wndw):
        super().__init__()
        self.title("Recover your account")
        self.geometry('250x350')
        self.resizable(width=NO, height=NO)

        self.wndw_back = wndw
        self.code = code

        self.canvas = tk.Canvas(self, bg="black", width=250, height=350)
        self.canvas.pack()

        self.MSSG = Label(self.canvas, text="", bg='Black', fg='red')
        self.MSSG.place(x=10, y=10)

        CodeL = Label(self.canvas, text='Enter the code sent to the email:', bg='green2', fg='Black')
        CodeL.place(x=10, y=50)

        CodeE = Entry(self.canvas, bg='black', fg='green2')
        CodeE.place(x=10, y=90)

        NewPasswordL = Label(self.canvas, text="Enter the new password", bg='green2', fg='Black')
        NewPasswordL.place(x=10, y=140)

        NewPasswordE = Entry(self.canvas, bg='black', fg='green2')
        NewPasswordE.place(x=10, y=180)

        ChangePasswordB = Button(self.canvas, text='Change password', bg='green1', fg='black',
                                 command=lambda: self.change_user_password(code=CodeE.get(),
                                                                           new_password=NewPasswordE.get()))
        ChangePasswordB.place(x=20, y=230)

        ExitB = Button(self.canvas, text='Exit', bg='green1', command=lambda: self.exit())
        ExitB.place(x=140, y=230)

        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')

    def change_user_password(self, code, new_password):
        if code == self.code:
            #Aqui va el codigo para reemplazar la contraseña en el archivo json

            print(f'Contraseña cambiada a {new_password}')

            self.destroy()
            self.wndw_back.deiconify()

        else:
            self.MSSG.config(text="Codigo incorrecto")
            self.canvas.update()


class password_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.random_code = None
        self.title("Recover your account")
        self.geometry('250x200')
        self.resizable(width=NO, height=NO)

        self.wndw_back = wndw

        self.canvas = tk.Canvas(self, bg="black", width=250, height=200)
        self.canvas.pack()

        self.MSSG = Label(self.canvas, text="", bg='Black', fg='red')
        self.MSSG.place(x=10, y=10)

        EmailL = Label(self.canvas, text='User Email to recover password:', bg='green2', fg='Black')
        EmailL.place(x=10, y=50)

        EmailE = Entry(self.canvas, bg='black', fg='green2')
        EmailE.place(x=10, y=90)

        SendCodepB = Button(self.canvas, text='Send Code to email', bg='green1', fg='black',
                            command=lambda: self.send_code(destinatario=EmailE.get()))
        SendCodepB.place(x=20, y=140)

        ExitB = Button(self.canvas, text='Exit', bg='green1', command=lambda: self.exit())
        ExitB.place(x=140, y=140)

        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')

    def send_code(self, destinatario):
        if destinatario:
            correo_manager = CM.CorreoManager(usuario="mendezariaspablo@gmail.com", password="zswt frhf gewi xzfu")
            self.random_code = ''.join(random.choices('0123456789', k=5))
            correo_manager.enviar_correo(destinatario=destinatario, asunto="Codigo de recuperacion de Galatec",
                                         mensaje=f"Su codigo para recuperar contraseña es: {self.random_code}")
            correo_manager.cerrar_sesion()
            self.withdraw()
            recover_password_wndw(wndw=self.wndw_back, code=self.random_code)

        else:
            self.MSSG.config(text="Correo inválido")
            self.canvas.update()

    def get_code(self):
        if self.random_code:
            return self.random_code

        else:
            return None

