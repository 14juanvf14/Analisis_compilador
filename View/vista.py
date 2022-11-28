import tkinter
from tkinter import *
from tkinter import messagebox as MessageBox

class Interface():
        
    def __init__(self, root):
        root.title("Regex Quiroga - Vasquez")
        root.config(bg="#1B2631")
        root.resizable(0, 0)
        root.eval('tk::PlaceWindow . center')
        
        miFrame = Frame()
        miFrame.pack(fill="both", expand=True)
        miFrame.config(bg="#1B2631")
        miFrame.config(width=500, height=700)
        
        
                
        labelEntero = Label(miFrame, text="digite número entero:",font=("courier", 12), justify=tkinter.CENTER)
        labelEntero.grid(row=1, column=1, pady=10, padx=10)
        labelEntero.config(fg="white",bg="#1B2631",font=("courier",12))
        variableTextEntero = StringVar()
        entryEntero = Entry(miFrame, bg="#F7F9F9", font=("courier",30), textvariable=variableTextEntero)
        entryEntero.grid(row=1, column=2,ipadx=30, ipady=20, padx=10, pady=10)
        Button(root, text="Valida entero", width=20, command=lambda : [self.comunicatorController(entryEntero.get(),1), variableTextEntero.set("")]).place(x=100, y=70)
    
        labelReal = Label(miFrame, text="digite número real :",font=("courier", 12), justify=tkinter.CENTER)
        labelReal.grid(row=3, column=1, pady=10, padx=10)
        labelReal.config(fg="white",bg="#1B2631",font=("courier",12))
        variableTextReal = StringVar()
        entryReal = Entry(miFrame, bg="#F7F9F9", font=("courier",30), textvariable=variableTextReal)
        entryReal.grid(row=3, column=2,ipadx=30, ipady=20, padx=10, pady=10)
        Button(root, text="Valida real", width=20, command=lambda : [self.comunicatorController(entryReal.get(),2), variableTextReal.set("")]).place(x=100, y=175)
        
        labelNotacion = Label(miFrame, text="digite notación científica:",font=("courier", 12), justify=tkinter.CENTER)
        labelNotacion.grid(row=5, column=1, pady=10, padx=10)
        labelNotacion.config(fg="white",bg="#1B2631",font=("courier",12))
        variableTextNotacion = StringVar()
        entryNotacion= Entry(miFrame, bg="#F7F9F9", font=("courier",30), textvariable=variableTextNotacion)
        entryNotacion.grid(row=5, column=2,ipadx=30, ipady=20, padx=10, pady=10)
        Button(root, text="Valida notación", width=20, command=lambda : [self.comunicatorController(entryNotacion.get(),3), variableTextNotacion.set("")]).place(x=100, y=280)
    
        labelCorreo = Label(miFrame, text="digite un correo :",font=("courier", 12), justify=tkinter.CENTER)
        labelCorreo.grid(row=7, column=1, pady=10, padx=10)
        labelCorreo.config(fg="white",bg="#1B2631",font=("courier",12))
        variableTextCorreo = StringVar()
        entryCorreo = Entry(miFrame, bg="#F7F9F9", font=("courier",30), textvariable=variableTextCorreo)
        entryCorreo.grid(row=7, column=2,ipadx=30, ipady=20, padx=10, pady=10)
        Button(root, text="Valida correo", width=20, command=lambda : [self.comunicatorController(entryCorreo.get(),4), variableTextCorreo.set("")]).place(x=100, y=385)


app = Tk()
window = Interface(app)
app.mainloop()