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
        
        
        
        self.canvas = tk.Canvas(self, bg="black", width=711, height=400)
        self.canvas.pack()
        
        SingleP_B = Button(self.canvas, text='Single Player',bg='green1',fg='black',command=lambda: self.S_ln())
        SingleP_B.place(x=20,y=180)

        MultiP_B = Button(self.canvas, text= ' Multiplayer ',bg='green1',fg='black',command=lambda: self.MP_ln())
        MultiP_B.place(x=20,y=220)
        
        Sttngs_B = Button(self.canvas, text='Game Settings', bg='green1',fg='black',command=lambda: self.STNGS())
        Sttngs_B.place(x=20,y=260)
        
        PodioG_B = Button(self.canvas, text='Podio', bg='green1', fg='black',command=lambda: self.PD())
        PodioG_B.place(x=20,y=300)
        
        ExitGm_B = Button(self.canvas, text='Exit Game', bg = 'green1', fg= 'black', command=lambda: self.destroy())
        ExitGm_B.place(x=20,y=340)

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

Menu_wndw()

