from tkinter import *
from User_Profile import User
import tkinter.filedialog as Fd
from tkinter import PhotoImage
from PIL import Image, ImageTk
import User_Profile as UP
import tkinter as tk
import JsonManager as JM
import CorreoManager as CM
import pygame
import sys
import os
import re

class singup_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Sing Up")
        self.geometry('650x500')
        self.resizable(width=NO, height=NO)
        SF = 20
        self.PrflPc = None
        self.shiPc = None
        self.MscDc = None

        self.wndw_back = wndw

        self.canvas = tk.Canvas(self, bg="black", width=650, height=500)
        self.canvas.pack()

        self.MSSG = Label(self.canvas, text="", bg='Black', fg='red', font=('Arial', SF))
        self.MSSG.place(x=10, y=10)

        NameL = Label(self.canvas, text='Real name:', bg='green2', fg='Black', font=('Arial', SF))
        NameL.place(x=10, y=50)

        NameE = Entry(self.canvas, bg='black', fg='green2', font=('Arial', SF))
        NameE.place(x=10, y=90)

        UserL = Label(self.canvas, text='Username:', bg='green2', fg='Black', font=('Arial', SF))
        UserL.place(x=10, y=140)

        UserE = Entry(self.canvas, bg='black', fg='green2', font=('Arial', SF))
        UserE.place(x=10, y=180)

        EmailL = Label(self.canvas, text='Email:', bg='green2', fg='Black', font=('Arial', SF))
        EmailL.place(x=10, y=230)

        EmailE = Entry(self.canvas, bg='black', fg='green2', font=('Arial', SF))
        EmailE.place(x=10, y=270)

        Pwrdl = Label(self.canvas, text='Password:', bg='green1', fg='black', font=('Arial', SF))
        Pwrdl.place(x=10, y=320)

        PwrdE = Entry(self.canvas, bg='black', fg='green2', font=('Arial', SF))
        PwrdE.place(x=10, y=360)

        PrPcB = Button(self.canvas, text='Profile Picture', bg='green2', fg='black', font=('Arial', SF-6), command=lambda: self.PrPc())
        PrPcB.place(x=400, y=20)

        self.PrPcL = Label(self.canvas, bg="black", image=None)
        self.PrPcL.place(x=400, y=60)

        SHIPB = Button(self.canvas, text="ship skin", bg="green2", fg="black", font=('Arial', SF-6), command=lambda: self.SHIP())                  
        SHIPB.place(x=400, y=250)
        
        self.SHIPL = Label(self.canvas, bg="black", image=None)
        self.SHIPL.place(x=400, y=300)

        MSCsB = Button(self.canvas, text="select song", bg="green2", fg='black', font=('Arial', SF-6), command=lambda: self.MSC(False))
        MSCsB.place(x=340, y=455)

        MSCmB = Button(self.canvas, text="select music", bg="green2",fg='black', font=('arial',SF-6), command=lambda: self.MSC(True))
        MSCmB.place(x=500,y=455)

        SingUpB = Button(self.canvas, text='SingUp', bg='green1', fg='black',font=('Arial', SF),
                         command=lambda: self.sign_up(email=EmailE.get(), user=UserE.get(), real_name=NameE.get(),
                                                      password=PwrdE.get(), prflP=self.PrflPc, shiP=self.shiPc, Mdrctr=self.MscDc))
        SingUpB.place(x=20, y=430), 

        ExitB = Button(self.canvas, text='Exit', bg='green1', command=lambda: self.exit(), font=('Arial', SF))
        ExitB.place(x=150, y=430)

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

    def sign_up(self, email, user, real_name, password, prflP, shiP, Mdrctr):
        correo_manager = CM.CorreoManager(usuario="mendezariaspablo@gmail.com", password="zswt frhf gewi xzfu")

        email = email.strip()
        user = user.strip()
        real_name = real_name.strip()
        password = password.strip()

        if len(email) > 0 and len(user) > 0 and len(real_name) > 0 and len(password) > 0:
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
