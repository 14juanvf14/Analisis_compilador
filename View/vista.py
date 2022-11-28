import tkinter
from tkinter import *
from tkinter import messagebox as MessageBox

class Interface():
        
    def __init__(self, root):
        root.title("Compilador Quiroga - Vasquez")
        root.config(bg="#1B2631")
        root.resizable(0, 0)
        
        miFrame = Frame()
        miFrame.pack(fill="both", expand=True)
        miFrame.config(bg="#1B2631")
        miFrame.config(width=1020, height=780)
        boton1 = Button(miFrame, text="Analisis Lexico")
        boton1.place(x=190, y=20, width=150, height=60)
        boton2 = Button(miFrame, text="Analisis Sintactico")
        boton2.place(x=530, y=20, width=150, height=60)
        boton3 = Button(miFrame, text="Analisis Sintactico")
        boton3.place(x=580, y=550, width=150, height=60)



app = Tk()
window = Interface(app)
app.mainloop()