from tkinter import *
from User_Profile import User
import User_Profile as UP
import tkinter as tk
import JsonManager as JM
import CorreoManager as CM
import pygame
import sys
import os


class recover_password_wndw(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recover your account")
        self.geometry('250x200')
        self.resizable(width=NO, height=NO)

        #.wndw_back = wndw

        self.canvas = tk.Canvas(self, bg="black", width=250, height=200)
        self.canvas.pack()

        self.MSSG = Label(self.canvas, text="", bg='Black', fg='red')
        self.MSSG.place(x=10, y=10)

        EmailL = Label(self.canvas, text='User Email to recover password:', bg='green2', fg='Black')
        EmailL.place(x=10, y=50)

        EmailE = Entry(self.canvas, bg='black', fg='green2')
        EmailE.place(x=10, y=90)

        SendCodepB = Button(self.canvas, text='Send Code to email', bg='green1', fg='black',
                         command=lambda: self.send_code())
        SendCodepB.place(x=20, y=140)

        ExitB = Button(self.canvas, text='Exit', bg='green1', command=lambda: self.exit())
        ExitB.place(x=140, y=140)

        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')

    def send_code(self):
        pass


recover_password_wndw()