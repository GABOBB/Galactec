from tkinter import *
import tkinter as tk


class v_help(tk.Tk):
    def __init__(self, wndw):
        super().__init__()
        self.title("Ayuda")
        self.geometry('600x600')
        self.resizable(width=NO, height=NO)

        self.wndw_back = wndw
        self.canvas = tk.Canvas(self, bg="black", width=600, height=600, bd=0, )
        self.canvas.pack()

        # BOTONES
        Exit_B = Button(self.canvas, text='exit', command=lambda: self.exit())
        Exit_B.place(x=520, y=550)

        # Fondo para el texto
        self.canvas.create_rectangle(10, 10, 590, 590, fill="gray")

        # Texto de ayuda
        help_text = """
        ¡Bienvenido a GalactaTec!

        Intenta sobrevivir el mayor tiempo posible sin que el enemigo te destruya. 
        No dejes que te impacten las balas del enemigo.

        Controles del juego:
        
        - Movimiento: Utiliza el joystick izquierdo para navegar por el espacio y esquivar obstáculos.
        
        - Ataque: Presiona el botón [A] para disparar balas y derrotar a los enemigos.
        
        - Defensa: Utiliza los bonus especiales para fortalecer tu defensa:
        
            - Y: Activa un escudo protector cuando lo necesites para protegerte de los ataques enemigos.
            - B: Presiona este botón para activar una vida extra y mantener tu aventura en curso.
            - X: Recolecta bonus para obtener puntos extra y aumentar tu puntaje.
            
            
        - Interacción: A lo largo del juego, podrás interactuar con bonificaciones que mejorarán 
          tu experiencia. 
          
          Simplemente acércate a ellas para recogerlas y obtener sus beneficios.
          
        - Menú: Para pausar el juego, presiona el botón [Start]. 
        
        Si necesitas salir del juego, puedes hacerlo presionando el botón [Select].
        
        

                                                          ¡Mucha suerte!
        """
        Help_Label = Label(self.canvas, text=help_text, bg='gray', fg='white', font=("Helvetica", 9), justify=LEFT)
        Help_Label.place(x=20, y=20)

        self.protocol("WM_DELETE_WINDOW", self.exit)
        self.mainloop()

    def exit(self):
        self.destroy()
        self.wndw_back.deiconify()
        print('exit')