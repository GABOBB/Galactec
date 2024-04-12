from tkinter import *
import tkinter as tk
import pygame
import sys

import os

class login:

    def __init__(self):
        
        self.__Menu=None#refers to the window (Tk)
        

    def cargarImagen(self,nombre):
        ruta = os.path.join('auxiliar',nombre)
        imagen = PhotoImage(file=ruta)
        return imagen

    def window(self):
        self.__Menu = Tk()
        self.__Menu.geometry('250x300')
        self.__Menu.title('LogIn')
        self.__Menu.resizable(width=NO,height=NO)
        self.__Menu.wm_attributes('-topmost',1)

        #Background = self.cargarImagen('fondo_menu.png')
        #labelBg = Label(self.__Menu,image=Background)
        #labelBg.pack()
        canvas = tk.Canvas(self.__Menu, bg="black", width=250, height=300)
        canvas.pack()
        
        
        cancel = Button(self.__Menu,text='Exit',bg='green1',command=self.__Menu.destroy)
        cancel.place(x=80,y=240)
        
        UserL=Label(self.__Menu, text='Username:',
                    bg='green2',fg='Black')
        UserL.place(x=15,y=50)

        UserE=Entry(bg='black',fg='green2')
        UserE.place(x=10,y=90)

        Pwrdl=Label(self.__Menu, text='Password:',
                    bg='green1',fg='black')
        Pwrdl.place(x=10,y=140)

        PwrdE=Entry(bg='black',fg='green2')
        PwrdE.place(x=10,y=180)

        LoginB = Button(self.__Menu, text= 'LogIn',bg='green1',fg='black',command=lambda: self.begin((UserE.get()),(PwrdE.get())))
        LoginB.place(x=20,y=240)

        self.__Menu.mainloop()

    def begin(self,X,y):
        print(X,y)
               


x = login()
x.window()