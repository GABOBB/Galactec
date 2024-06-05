from tkinter import *
import tkinter as tk
import v_ayuda as VA
import pygame
import sys
import os

class Stngs_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Configuración del Juego")
        self.geometry('750x500')
        self.resizable(width=NO, height=NO)

        self.wndw_back = wndw
        self.canvas = tk.Canvas(self, bg="#303030", width=750, height=500, bd=0)
        self.canvas.pack()

        # Botones
        Exit_B = Button(self.canvas, text='Exit', bg='#1e1e1e', fg='white', font=('Helvetica', 12, 'bold'), command=lambda: self.exit())
        Exit_B.place(x=650, y=400, width=80, height=30)

        Titulo = Label(self.canvas, text='Selecciona el patrón del enemigo:', bg='#303030', fg='white', font=("Helvetica", 16, "bold"))
        Titulo.place(x=200, y=30)

        Patrones_frame = Frame(self.canvas, bg="#303030", bd=0)
        Patrones_frame.place(x=50, y=100)

        Patron_A = Button(Patrones_frame, text='Patrón A', bg='green', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Patron_A.grid(row=0, column=0, padx=10, pady=10)

        Patron_B = Button(Patrones_frame, text='Patrón B', bg='green', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Patron_B.grid(row=0, column=1, padx=10, pady=10)

        Patron_C = Button(Patrones_frame, text='Patrón C', bg='green', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Patron_C.grid(row=0, column=2, padx=10, pady=10)

        Patron_D = Button(Patrones_frame, text='Patrón D', bg='green', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Patron_D.grid(row=0, column=3, padx=10, pady=10)

        Patron_E = Button(Patrones_frame, text='Patrón E', bg='green', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Patron_E.grid(row=0, column=4, padx=10, pady=10)

        # Botones niveles
        Nivel_frame = Frame(self.canvas, bg="#303030", bd=0)
        Nivel_frame.place(x=600, y=150)

        Nivel1_boton = Button(Nivel_frame, text="Nivel 1", bg='blue', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Nivel1_boton.grid(row=0, column=0, padx=10, pady=10)

        Nivel2_boton = Button(Nivel_frame, text="Nivel 2", bg='blue', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Nivel2_boton.grid(row=1, column=0, padx=10, pady=10)

        Nivel3_boton = Button(Nivel_frame, text="Nivel 3", bg='blue', fg='white', font=("Helvetica", 12, "bold"), command=lambda: self.exit())
        Nivel3_boton.grid(row=2, column=0, padx=10, pady=10)

        # Botón de ayuda
        self.HELP_B = Button(self.canvas, text='HELP', bg='#1e1e1e', fg='white', font=("Helvetica", 12, "bold"), command=lambda: VA.v_help(self))
        self.HELP_B.place(x=20, y=20, width=80, height=30)

        self.protocol("WM_DELETE_WINDOW", self.exit)
        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()