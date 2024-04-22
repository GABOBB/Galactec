from tkinter import *
import tkinter as tk

class v_help (tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Ayuda")
        self.geometry('500x500')
        self.resizable(width=NO, height=NO)
        #image_fondo = PhotoImage(file="Imagenes/Auxiliares/setting_image.png")

        self.wndw_back = wndw
        self.canvas = tk.Canvas(self, bg="black", width=500, height=500, bd=0, )

        self.canvas.pack()

        # BOTONES
        Exit_B = Button(self.canvas, text='exit', command=lambda: self.exit())
        Exit_B.place(x=450, y=450)

        Titulo = Label(self.canvas, text='Intenta sobrevivir el mayor tiempo posible sin que el enemigo te destruya \n No dejes que te impacten las balas del enemigo \n\nPara sobrevivir tienes que usar \nlas teclas de dirección para moverte y el boton de espcacio para impulsar tus balas. \n\n Habrán sorpresas conforme avances en el juego. \n\n¡Mucha suerte! ', bg='green2', fg='Black')
        Titulo.place(x=30, y=50)
        
        self.protocol("WM_DELETE_WINDOW", self.exit)
        
        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')