from tkinter import *
from User_Profile import User
import tkinter.filedialog as Fd
from tkinter import PhotoImage
from PIL import Image, ImageTk
import User_Profile as UP
import tkinter as tk
import JsonManager as JM
import CorreoManager as CM
import v_ayuda as VA
import pygame
import sys
import os
import re

class singup_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Sing Up")
        self.geometry('850x600')
        self.resizable(width=NO, height=NO)
        SF = 20
        self.PrflPc = None
        self.shiPc = None
        self.MscDc = None
        self.last_email = None
        self.code = None

        self.wndw_back = wndw

        self.canvas = tk.Canvas(self, bg="black", width=850, height=600)
        self.canvas.pack()

        SF = 12  # Tamaño de fuente común

        self.MSSG = Label(self.canvas, text="", bg='black', fg='red', font=('Arial', SF))
        self.MSSG.place(x=10, y=10)

        NameL = Label(self.canvas, text='Real name:', bg='green', fg='white', font=('Arial', SF))
        NameL.place(x=10, y=50)

        NameE = Entry(self.canvas, bg='black', fg='white', font=('Arial', SF))
        NameE.place(x=10, y=90)

        UserL = Label(self.canvas, text='Username:', bg='green', fg='white', font=('Arial', SF))
        UserL.place(x=10, y=140)

        UserE = Entry(self.canvas, bg='black', fg='white', font=('Arial', SF))
        UserE.place(x=10, y=180)

        EmailL = Label(self.canvas, text='Email:', bg='green', fg='white', font=('Arial', SF))
        EmailL.place(x=10, y=230)

        EmailE = Entry(self.canvas, bg='black', fg='white', font=('Arial', SF))
        EmailE.place(x=10, y=270)

        Pwrdl = Label(self.canvas, text='Password:', bg='green', fg='white', font=('Arial', SF))
        Pwrdl.place(x=10, y=320)

        PwrdE = Entry(self.canvas, bg='black', fg='white', font=('Arial', SF))
        PwrdE.place(x=10, y=360)

        PrPcB = Button(self.canvas, text='Profile Picture', bg='green', fg='white', font=('Helvetica', SF),
                       command=lambda: self.PrPc())
        PrPcB.place(x=400, y=20)

        self.PrPcL = Label(self.canvas, bg="black", image=None)
        self.PrPcL.place(x=400, y=60)

        SHIPB = Button(self.canvas, text="Ship Skin", bg="green", fg="white", font=('Helvetica', SF),
                       command=lambda: self.SHIP())
        SHIPB.place(x=600, y=20)

        self.SHIPL = Label(self.canvas, bg="black", image=None)
        self.SHIPL.place(x=600, y=60)

        MSCsB = Button(self.canvas, text="Select Song", bg="green", fg='white', font=('Helvetica', SF),
                       command=lambda: self.MSC(False))
        MSCsB.place(x=340, y=535)

        MSCmB = Button(self.canvas, text="Select Music", bg="green", fg='white', font=('Helvetica', SF),
                       command=lambda: self.MSC(True))
        MSCmB.place(x=500, y=535)

        SendEmailCodeB = Button(self.canvas, text='Send Code', bg='green', fg='white', font=('Helvetica', SF),
                                command=lambda: self.SendCode(EmailE.get()))
        SendEmailCodeB.place(x=350, y=270)

        EmailCode = Label(self.canvas, text='Email Verification Code', bg='green', fg='white', font=('Arial', SF))
        EmailCode.place(x=10, y=410)

        EmailCodeE = Entry(self.canvas, bg='black', fg='white', font=('Arial', SF))
        EmailCodeE.place(x=10, y=450)

        SingUpB = Button(self.canvas, text='SignUp', bg='green', fg='white', font=('Helvetica', SF),
                         command=lambda: self.sign_up(email=EmailE.get(), user=UserE.get(), real_name=NameE.get(),
                                                      password=PwrdE.get(), prflP=self.PrflPc, shiP=self.shiPc,
                                                      Mdrctr=self.MscDc, code=EmailCodeE.get()))
        SingUpB.place(x=20, y=530)

        self.HELP_B = Button(self.canvas, text='HELP', bg='green', fg='white', command=lambda: VA.v_help(self),
                             font=('Arial', SF))
        self.HELP_B.place(x=750, y=20)

        ExitB = Button(self.canvas, text='Exit', bg='green', fg='white', command=lambda: self.exit(),
                       font=('Arial', SF))
        ExitB.place(x=150, y=530)

        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')

    def PrPc(self):
        file_path = Fd.askopenfilename(title="Select Profile Picture", initialdir='/', filetypes=[("Image files", "*.png *.gif *.jpg *.jpeg")])
        
        
        if file_path:
            self.PrflPc =file_path
            # Abrir la imagen y redimensionarla
            img = Image.open(file_path)
            img = img.resize((100, 100), Image.LANCZOS)  # Cambia (100, 100) al tamaño deseado
            
            # Convertirla en un objeto PhotoImage
            img = ImageTk.PhotoImage(img)

            # Configurar el Label con la imagen
            self.PrPcL.config(image=img)
            self.PrPcL.image = img  # Necesario para evitar que la imagen sea recolectada por el garbage collector
            
    def SHIP(self):
        file_path = Fd.askopenfilename(title='Select Ship skin', initialdir='/', filetypes=[("Image files", "*.png *.jpg *.gif *.jpeg")])
        
        if file_path:
            self.shiPc =file_path
            img = Image.open(file_path)
            img = img.resize((100, 100), Image.LANCZOS)
        
            img = ImageTk.PhotoImage(img)

            self.SHIPL.config(image=img)
            self.SHIPL.imge = img
            
    def MSC(self, indicator):
        if(indicator):
            file_path = Fd.askdirectory(title='select folder of music', initialdir='/')
        else:
            file_path = Fd.askopenfilename(title='Select Ship skin', initialdir='/', filetypes=[("MP3 files", "*.mp3")])

        self.MscDc = file_path
        print(self.MscDc)            

    def SendCode(self, email):
        correo_manager = CM.CorreoManager(usuario="mendezariaspablo@gmail.com", password="zswt frhf gewi xzfu")

        if len(email) > 0 and '@' in email and '.' in email and email.count('@'):
            if email != self.last_email:
                self.code = correo_manager.verificar_correo(email)
                if self.code:
                    self.last_email = email
                    self.MSSG.config(text="Codigo enviado a su correo")
                    self.canvas.update()
                else:
                    self.MSSG.config(text="Correo inválido")
                    self.canvas.update()
            else:
                self.MSSG.config(text="El codigo ya fue enviado a este correo")
                self.canvas.update()
        else:
            self.MSSG.config(text="Correo inválido")
            self.canvas.update()
        correo_manager.cerrar_sesion()

    def CodeValidation(self, code):
        if code == self.code:
            return True
        else:
            self.MSSG.config(text="Codigo de verificacion incorrecto")
            return False
        

    def sign_up(self, email, user, real_name, password, prflP, shiP, Mdrctr, code):
        correo_manager = CM.CorreoManager(usuario="mendezariaspablo@gmail.com", password="zswt frhf gewi xzfu")

        email = email.strip()
        user = user.strip()
        real_name = real_name.strip()
        password = password.strip()

        if len(email) > 0 and len(user) > 0 and len(real_name) > 0 and len(password) > 0 and len(code) >= 0:
            Tiene_M = any(c.isupper() for c in password)
            Tiene_m = any(c.islower() for c in password)
            Tiene_N = any(c.isdigit() for c in password)
            Tiene_C = bool(re.search('[^A-Za-z0-9]', password))
            if(len(password) > 6 and Tiene_M and Tiene_m and Tiene_N and Tiene_C):
                U = UP.User(real_name, user, password, email, prflP, shiP, Mdrctr)
                jm = JM.JSONManager('usuarios.json')
                L = jm.cargar_lista(User)
                print(L)
                Check = 'correcto'
                for l in L:
                    print(l.get_USR() + '---' + user)
                    if(l.get_USR() == user):
                        Check = 'usuario'
                        break
                    if(l.get_CRR() == email):
                        Check = 'mail'
                        break
                if(Check == 'correcto'):
                    if self.CodeValidation(code):
                        self.destroy()
                        print(len(L))
                        L += [U]
                        print(len(L))
                        jm.guardar_lista(L)
                        self.wndw_back.deiconify()
                        correo_manager.cerrar_sesion()
                elif(Check == 'User'):
                    self.MSSG.config(text="Usuario ya existe")
                    self.canvas.update()
                elif(Check == 'mail'):
                    self.MSSG.config(text="El correo se Uso")
                    self.canvas.update()
            elif(len(password) < 7):
                print(len(password))
                self.MSSG.config(text='Contraseña muy corta')
                self.canvas.update()
            elif(not Tiene_m or not Tiene_M):
                print(not Tiene_m or not Tiene_M)
                self.MSSG.config(text="La contraseña debe tener mayuscula\ny minusculas")
                self.canvas.update()
            elif(not Tiene_N):
                print()
                self.MSSG.config(text="la contraseña debe tener Numeros")
                self.canvas.update()
            elif(not Tiene_C):
                self.MSSG.config(text="la contraseña debe tener caracte especial")
                self.canvas.update()
        else:
            self.MSSG.config(text="Credenciales incompletas")
            self.canvas.update()

        correo_manager.cerrar_sesion()
#x = singup_wndw(None)
