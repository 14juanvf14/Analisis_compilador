import tkinter
from tkinter import *
from tkinter import font as font
from tkinter import messagebox as MessageBox

class Interface():
        
    def __init__(self, root):
        root.title("Compilador Quiroga - Vasquez")
        root.config(bg="#1B2631")
        root.resizable(0, 0)
        
        miFrame = Frame()
        miFrame.pack(fill="both", expand=True)
        miFrame.config(bg="#1B2631")
        miFrame.config(width=1020, height=720)

        label1 = Label(miFrame, background="#FFF")
        label1.place(x=90, y=50, width=800, height=5)

        myFont= font.Font(family='Roboto', size=12)
        myFont2= font.Font(family='Roboto', size=14)

        boton1 = Button(miFrame, text="Analisis \nLexico", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        boton1['font']=myFont
        boton1.place(x=90, y=20, width=150, height=60)
        boton2 = Button(miFrame, text="Analisis \nSintactico", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        boton2['font']=myFont
        boton2.place(x=430, y=20, width=150, height=60)
        boton3 = Button(miFrame, text="Generar \nrespuesta", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        boton3['font']=myFont
        boton3.place(x=770, y=20, width=150, height=60)

        entryOracion = Entry(miFrame)
        entryOracion['font'] = myFont2
        entryOracion.place(x=90, y=120, width=600, height=50)

        entryTkLexico1 = Entry(miFrame, state='readonly')
        entryTkLexico1['font'] = myFont2
        entryTkLexico1.place(x=90, y=180, width=600, height=50)

        entryTkLexicoConfirma = Entry(miFrame, state='readonly')
        entryTkLexicoConfirma['font'] = myFont2
        entryTkLexicoConfirma.place(x=90, y=240, width=600, height=50)

        entryTkLexico2 = Entry(miFrame, state='readonly')
        entryTkLexico2['font'] = myFont2
        entryTkLexico2.place(x=90, y=300, width=600, height=50)

        entrySintactico = Entry(miFrame, state='readonly')
        entrySintactico['font'] = myFont2
        entrySintactico.place(x=90, y=360, width=600, height=50)

        entryRespuesta = Entry(miFrame, state='readonly')
        entryRespuesta['font'] = myFont2
        entryRespuesta.place(x=90, y=420, width=600, height=50)

        entryTkRespuesta1 = Entry(miFrame, state='readonly')
        entryTkRespuesta1['font'] = myFont2
        entryTkRespuesta1.place(x=90, y=480, width=600, height=50)

        entryTkRespuesta2 = Entry(miFrame, state='readonly')
        entryTkRespuesta2['font'] = myFont2
        entryTkRespuesta2.place(x=90, y=540, width=600, height=50)

        entryErrorLexico= Entry(miFrame, state='readonly')
        entryErrorLexico['font'] = myFont2
        entryErrorLexico.place(x=720, y=180, width=200, height=110)

        entryErrorSintactico= Entry(miFrame, state='readonly')
        entryErrorSintactico['font'] = myFont2
        entryErrorSintactico.place(x=720, y=360, width=200, height=110)

        label2 = Label(miFrame, background="#FFF")
        label2.place(x=90, y=670, width=800, height=5)

        boton3 = Button(miFrame, text="Cargar \nPreguntas", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        boton3['font']=myFont
        boton3.place(x=90, y=640, width=150, height=60)
        boton4 = Button(miFrame, text="Cargar \nRespuestas", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        boton4['font']=myFont
        boton4.place(x=430, y=640, width=150, height=60)
        boton5 = Button(miFrame, text="Cargar \nT Simbolos", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        boton5['font']=myFont
        boton5.place(x=770, y=640, width=150, height=60)

        label3 = Label(miFrame, background="#1B2631", text="O", foreground="#FFF")
        label3['font']=myFont2
        label3.place(x=40, y=130)

        label4 = Label(miFrame, background="#1B2631", text="Tk1", foreground="#FFF")
        label4['font']=myFont2
        label4.place(x=40, y=190)

        label5 = Label(miFrame, background="#1B2631", text="AL", foreground="#FFF")
        label5['font']=myFont2
        label5.place(x=40, y=250)

        label5 = Label(miFrame, background="#1B2631", text="Tk2", foreground="#FFF")
        label5['font']=myFont2
        label5.place(x=40, y=310)

        label6 = Label(miFrame, background="#1B2631", text="AS", foreground="#FFF")
        label6['font']=myFont2
        label6.place(x=40, y=370)

        label7 = Label(miFrame, background="#1B2631", text="Rp", foreground="#FFF")
        label7['font']=myFont2
        label7.place(x=40, y=430)

        label8 = Label(miFrame, background="#1B2631", text="Tk1", foreground="#FFF")
        label8['font']=myFont2
        label8.place(x=40, y=490)

        label9 = Label(miFrame, background="#1B2631", text="Tk2", foreground="#FFF")
        label9['font']=myFont2
        label9.place(x=40, y=550)

        label10 = Label(miFrame, background="#1B2631", text="Error Lexico", foreground="#FFF")
        label10['font']=myFont2
        label10.place(x=720, y=140)

        label10 = Label(miFrame, background="#1B2631", text="Error Sintactico", foreground="#FFF")
        label10['font']=myFont2
        label10.place(x=720, y=320)




app = Tk()
window = Interface(app)
app.mainloop()