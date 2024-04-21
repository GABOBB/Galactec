from tkinter import *
import tkinter as tk
import pygame
import sys
import os

class Stngs_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Game Setings")
        self.geometry('750x500')
        self.resizable(width=NO,height=NO)
        image_fondo = PhotoImage(file="Imagenes/Auxiliares/setting_image.png")

        self.wndw_back = wndw
        self.canvas = tk.Canvas(self,bg= "black",width=750, height=500,bd=0,)

        self.canvas.pack()

        #BOTONES
        Exit_B = Button(self.canvas,text='exit',command=lambda: self.exit())
        Exit_B.place(x=400, y=700)

        Titulo = Label(self.canvas, text='Seleccione el patron del enemigo', bg='green2', fg='Black')
        Titulo.place(x=250, y=50)


        Patron_A = Button(self.canvas, text='Patron  A', command=lambda: self.exit())
        Patron_A.place(x=50, y=400)


        Patron_B = Button(self.canvas, text='Patron B', command=lambda: self.exit())
        Patron_B.place(x=150, y=400)


        Patron_C = Button(self.canvas, text='Patron C', command=lambda: self.exit())
        Patron_C.place(x=250, y=400)

        Patron_D = Button(self.canvas, text='Patron D', command=lambda: self.exit())
        Patron_D.place(x=350, y=400)


        Patron_E = Button(self.canvas, text='Patron E', command=lambda: self.exit())
        Patron_E.place(x=450, y=400)

        #Botones niveles
        #Nivel1_boton = Button(self.canvas, text="Nivel1", bg='green1',fg='black', command=lambda: self.exit())
        #Nivel1_boton.place(x=500, y=500)


        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')