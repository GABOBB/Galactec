from tkinter import *
import tkinter as tk
import pygame
import sys
import os

class Podio_wndw(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Podio historico")
        self.geometry('750x500')
        self.resizable(width=NO,height=NO)
        
        self.wndw_back = wndw
        
        Exit_B = Button(self,text='exit',command=lambda: self.exit())
        Exit_B.pack()
        
        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')
        
#Podio_wndw()