from tkinter import *
import tkinter as tk
import pygame
import sys
import os
import v_ayuda as VA

class Podio_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Podio historico")
        self.geometry('750x500')
        self.resizable(width=NO,height=NO)
        
        self.wndw_back = wndw
        
        Exit_B = Button(self,text='exit',command=lambda: self.exit())
        Exit_B.pack()

        self.HELP_B = Button(self, text='HELP', bg='green1', fg='black', command=lambda: VA.v_help(self)) # Cambiar la palabra canva cuando se agregue un canva o lo que se vea en pantalla
        self.HELP_B.place(x=700, y=5)


        self.protocol("WM_DELETE_WINDOW", self.exit)
        
        self.mainloop()


    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')
        
#Podio_wndw()