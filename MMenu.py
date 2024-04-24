import time
import tkinter as tk
from tkinter import *
from User_Profile import User
import JsonManager
import Setings as Stngs
import logIn as LGIN
import Podio as PD
import v_ayuda as VA
import sys
import os
import Game


class Menu_wndw(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title('GalaTec')
        self.geometry('711x400')
        self.resizable(width=NO,height=NO)
        self.wm_attributes('-topmost',1)
        
        
        self.user1 = None
        self.user2 = None
        self.C_U1 = None
        self.C_U2 = None
        
        self.canvas = tk.Canvas(self, bg="black", width=711, height=400,bd=0, highlightthickness=0)
        self.canvas.pack()
        
        self.FirstP_B = Button(self.canvas, text='First Player',bg='green1',fg='black',command=lambda: self.S_ln())
        self.FirstP_B.place(x=20,y=180)

        self.SecndP_B = Button(self.canvas, text= ' Multiplayer ',bg='green1',fg='black',command=lambda: self.MP_ln())
        self.SecndP_B.place(x=20,y=220)
        self.SecndP_B.config(state=tk.DISABLED)
        
        self.Sttngs_B = Button(self.canvas, text='Game Settings', bg='green1',fg='black',command=lambda: self.STNGS())
        self.Sttngs_B.place(x=20,y=260)
        
        self.PodioG_B = Button(self.canvas, text='Podio', bg='green1', fg='black',command=lambda: self.PD())
        self.PodioG_B.place(x=20,y=300)
        
        self.ExitGm_B = Button(self.canvas, text='Exit Game', bg = 'green1', fg= 'black', command=lambda: self.destroy())
        self.ExitGm_B.place(x=20,y=340)

        self.HELP_B = Button(self.canvas, text='HELP', bg='green1', fg='black', command=lambda: self.VA())
        self.HELP_B.place(x=650, y=20)

        self.mainloop()
        
        
    def cargarImagen(self,nombre):
        ruta = os.path.join('auxiliar',nombre)
        imagen = PhotoImage(file=ruta)
        return imagen
    
  
    def S_ln(self):
        if self.user1 != None:
            self.user1 = None
            self.C_U1.destroy()
        
        x = LGIN.login_wndw(self)
        
    
    def MP_ln(self):
        self.user2 = None
        self.withdraw()
        LGIN.login_wndw(self)
    
    def STNGS(self):
        self.withdraw()
        Stngs.Stngs_wndw(self)

    def VA(self):
        self.withdraw()
        VA.v_help(self)
        
    def PD(self):
        self.withdraw()
        PD.Podio_wndw(self)

    def Log_out(self,x,c):
        self.withdraw()
        if(x==250):
            c.destroy()
            self.user1=None
            if(self.user2 != None):
                self.confirmed(self.user2)
                self.C_U2.destroy()
                self.user2 = None
                self.update() 
            else:
                self.SecndP_B.config(state=tk.DISABLED)
        else:
            c.destroy()
            self.user2 = None
            self.C_U2 = None
            
        '''
        c.destroy()
        if x == 250:
            print("se borra el priemro")
            self.User1 = None
            if(self.user2 == None):
                self.SecndP_B.config(state=tk.DISABLED)
            else:
                print("hola si detecta que no es nulo") 
                self.C_U2.destroy()           
                time.sleep(5)
                print('se tubo que borrar el segundo')
                self.confirmed(self.user2)           
                self.user2 = None
        else:
            self.user2 = None
            self.C_U2 = None'''
    
    def play(self):
        self.withdraw()
        Game.Game()
    
    def STTNGS(self,X):
        #self.withdraw()
        if(X==250):
            CDU = c_D_u(self.user1,self, X)
        else:
            CDU = c_D_u(self.user2,self, X)
        
        
    
    def confirmed(self, User):
        
        canvas_user = tk.Canvas(self, bg="Black", width=250, height=300,bd=0, highlightthickness=0)
        if(self.user1 == None):
            X = 250
            self.C_U1 = canvas_user
            self.user1 = User
            Start_Game_B = Button(canvas_user, text='Start',bg='Green1',fg='black', command=lambda: self.play())
            Start_Game_B.place(x=60,y=260)
        else:
            X = 450 
            self.C_U2 = canvas_user
            self.user2 = User
            print(self.C_U2 == None)
        canvas_user.place(x=X,y=0)
        
        #FotoL = Label(canvas_user,image=PhotoImage(file=User.get_FT()))
        #FotoL.place(x=60,y=10)
        
        print(User.get_USR())
        UserL = Label(canvas_user, text=User.get_USR(),bg='black',fg='green1')
        UserL.place(x=60,y=140)
        
        print(User.get_NMBR())
        NameL = Label(canvas_user, text=User.get_NMBR(),bg='black',fg='green1')
        NameL.place(x=60,y=170)
        
        print(User.get_CRR())
        MailL = Label(canvas_user, text=User.get_CRR(),bg='black',fg='green1')
        MailL.place(x=60,y=200) 
        
        Log_Out_B = Button(canvas_user, text='Log Out',fg='black',bg='green1',command=lambda: self.Log_out(X,canvas_user),bd=0)
        Log_Out_B.place(x=60,y=230)
        
        settings_B = Button(canvas_user, text = 'user settings',fg='green1',bg='black',command=lambda: self.STTNGS(X),bd=0)
        settings_B.place(x=60,y=280)
         
        self.SecndP_B.config(state=tk.NORMAL)
        print('se confirmaron las credenciales')

Menu_wndw()

class c_D_u(tk.Tk):

    def __init__(self,User,wndwB, indicador):
        self.user = User
        super().__init__()
        
        self.title('configuracion de usuario')
        self.geometry('300x500')
        self.resizable(width=NO,height=NO)
        self.wm_attributes('-topmost',1)

        self.canvas = tk.Canvas(self, bg="black", width=300, height=500, highlightthickness=0)
        self.canvas.pack()
        
        self.wndwB = wndwB
        self.indcdr = indicador
        
        NameL = Label(self.canvas, text='Real name:', bg='green2', fg='Black')
        NameL.place(x=10, y=50)

        NameE = Entry(self.canvas, bg='black', fg='green2')
        NameE.config(text=self.user.get_NMBR())
        NameE.place(x=10, y=90)

        UserL = Label(self.canvas, text='Username:', bg='green2', fg='Black')
        UserL.place(x=10, y=140)

        UserE = Entry(self.canvas, bg='black', fg='green2')
        UserE.config(text=self.user.get_USR())
        UserE.place(x=10, y=180)

        EmailL = Label(self.canvas, text='Email:', bg='green2', fg='Black')
        EmailL.place(x=10, y=230)

        EmailE = Entry(self.canvas, bg='black', fg='green2')
        EmailE.config(text=self.user.get_CRR())
        EmailE.place(x=10, y=270)

        Pwrdl = Label(self.canvas, text='Password:', bg='green1', fg='black')
        Pwrdl.place(x=10, y=320)

        PwrdE = Entry(self.canvas, bg='black', fg='green2')
        PwrdE.config(texte=self.user.get_PSSWRD())
        PwrdE.place(x=10, y=360)

        change_B = Button(self.canvas, bg='green1', fg='black', command=lambda: self.reescribir_D(NameE.get(), 
                                                                                             UserE.get(),
                                                                                             EmailE.get(),
                                                                                             PwrdE.get()))
        change_B.place(x=15,y=460)

        self.mainloop()

    def reescribir_D(self, name, user, email, psswrd):
        new_user = User(name, user, psswrd, email, None, None, None)
        l = JsonManager.JSONManager.cargar_lista('usuarios.json')
        for i in l:
            if(i == self.user):
                i = new_user
                break
        JsonManager.JSONManager.guardar_lista(l)
        if(self.indcdr == 250):
            self.wndwB.user1 = None
            self.wndwB.confirmed(new_user)
        else:
            self.wndwB.user2 = None
            self.wndwB.confirmed(new_user)