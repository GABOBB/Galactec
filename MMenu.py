import tkinter as tk
from tkinter import *
import Setings as Stngs
import logIn as LGIN
import Podio as PD
import sys
import os


class Menu_wndw(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title('GalaTec')
        self.geometry('711x400')
        self.resizable(width=NO,height=NO)
        self.wm_attributes('-topmost',1)
        
        
        self.user1 = None
        self.canvas_user1 = None
        self.user2 = None
        self.canvas_user2 = None
        
        
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

        self.mainloop()
        
        
    def cargarImagen(self,nombre):
        ruta = os.path.join('auxiliar',nombre)
        imagen = PhotoImage(file=ruta)
        return imagen
    
  
    def S_ln(self):
        self.withdraw()
        x = LGIN.login_wndw(self)
        if(x):
            print('si sale true')
        else:
            print('no se si llega None')
    
    def MP_ln(self):
        self.withdraw()
        LGIN.login_wndw(self)
    
    def STNGS(self):
        self.withdraw()
        Stngs.Stngs_wndw(self)
        
    def PD(self):
        self.withdraw()
        PD.Podio_wndw(self)

    def confirmed(self):#, User):
        #self.user = User
        self.canvas_user1 = tk.Canvas(self, bg="black", width=300, height=400,bd=0, highlightthickness=0)
        self.canvas_user1.place(x=450,y=0)
        
        UserL = Label(self.canvas_user1, text='User.get_USR()',bg='black',fg='green1')
        UserL.place(x=60,y=140)
        
        NameL = Label(self.canvas_user1, text='User.get_NMBR()',bg='black',fg='green1')
        NameL.place(x=60,y=170)
        
        MailL = Label(self.canvas_user1, text='User.get_CRR()',bg='black',fg='green1')
        MailL.place(x=60,y=200) 
        
        Begin_Game_B = Button(self.canvas_user1, text='Start game',fg='black',bg='green1',command=print("hola"),bd=0)
        Begin_Game_B.place(x=60,y=230)
        
        self.SecndP_B.config(state=tk.NORMAL)
        print('se confirmaron las credenciales')
        
        
        
Menu_wndw()

