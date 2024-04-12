import tkinter as tk
from tkinter import *
import logIn as LGIN
import sys
import os


class MMenu:

    def __init__(self):
        self.__Menu=None#refers to the window (Tk)
        self.canvas = None
        
    def cargarImagen(self,nombre):
        ruta = os.path.join('auxiliar',nombre)
        imagen = PhotoImage(file=ruta)
        return imagen
    
  
    def Sln(self):
        L = LGIN.login(self.canvas)
        Log_C = L.get_C()
        self.canvas.destroy()
        self.canvas = Log_C
    
    def Sln2(self):
        L2 = LGIN.login()
        Log2_C = L2.get_C()
        self.canvas2 = Log2_C
        self.canvas.place(x=500,y=10)    
    

    def window(self):
        print(3)
        self.__Menu = Tk()
        self.__Menu.geometry('711x400')
        self.__Menu.title('MAIN_MENU')
        self.__Menu.resizable(width=NO,height=NO)
        self.__Menu.wm_attributes('-topmost',1)

        self.canvas = tk.Canvas(self.__Menu, bg="black", width=711, height=400)
        self.canvas.pack()
        
        SingleP_B= Button(self.canvas, text='Single Player',bg='green1',fg='black',command=lambda: self.Sln())
        SingleP_B.place(x=20,y=180)

        MultiP_B = Button(self.canvas, text= ' Multiplayer ',bg='green1',fg='black',command=lambda: self.Sln2())
        MultiP_B.place(x=20,y=220)
        
        Sttngs_B = Button(self.canvas, text='Game Settings', bg='green1',fg='black')
        Sttngs_B.place(x=20,y=260)
        
        PodioG_B = Button(self.canvas, text='Podio', bg='green1', fg='black')
        PodioG_B.place(x=20,y=300)
        
        ExitGm_B = Button(self.canvas, text='Exit Game', bg = 'green1', fg= 'black', command=lambda: self.__Menu.destroy())
        ExitGm_B.place(x=20,y=340)

        self.__Menu.mainloop()


M=MMenu()
M.window()
