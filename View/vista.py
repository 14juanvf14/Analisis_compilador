import tkinter
from tkinter import *
from tkinter import font as font
import csv

class Interface():
        
    def __init__(self, root):
        root.title("Compilador Quiroga - Vasquez")
        root.config(bg="#1B2631")
        root.resizable(0, 0)
        
        self.miFrame = Frame()
        self.miFrame.pack(fill="both", expand=True)
        self.miFrame.config(bg="#1B2631")
        self.miFrame.config(width=1020, height=720)

        self.label1 = Label(self.miFrame, background="#FFF")
        self.label1.place(x=90, y=50, width=800, height=5)

        self.myFont= font.Font(family='Roboto', size=12)
        self.myFont2= font.Font(family='Roboto', size=14)

        self.boton1 = Button(self.miFrame, text="Analisis \nLexico", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        self.boton1['font']=self.myFont
        self.boton1.place(x=90, y=20, width=150, height=60)
        self.boton2 = Button(self.miFrame, text="Analisis \nSintactico", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        self.boton2['font']=self.myFont
        self.boton2.place(x=430, y=20, width=150, height=60)
        self.boton3 = Button(self.miFrame, text="Generar \nrespuesta", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        self.boton3['font']=self.myFont
        self.boton3.place(x=770, y=20, width=150, height=60)

        self.entryOracion = Entry(self.miFrame)
        self.entryOracion['font'] = self.myFont2
        self.entryOracion.place(x=90, y=120, width=600, height=50)

        self.entryTkLexico1 = Entry(self.miFrame, state='readonly')
        self.entryTkLexico1['font'] = self.myFont2
        self.entryTkLexico1.place(x=90, y=180, width=600, height=50)

        self.entryTkLexicoConfirma = Entry(self.miFrame, state='readonly')
        self.entryTkLexicoConfirma['font'] = self.myFont2
        self.entryTkLexicoConfirma.place(x=90, y=240, width=600, height=50)

        self.entryTkLexico2 = Entry(self.miFrame, state='readonly')
        self.entryTkLexico2['font'] = self.myFont2
        self.entryTkLexico2.place(x=90, y=300, width=600, height=50)

        self.entrySintactico = Entry(self.miFrame, state='readonly')
        self.entrySintactico['font'] = self.myFont2
        self.entrySintactico.place(x=90, y=360, width=600, height=50)

        self.entryRespuesta = Entry(self.miFrame, state='readonly')
        self.entryRespuesta['font'] = self.myFont2
        self.entryRespuesta.place(x=90, y=420, width=600, height=50)

        self.entryTkRespuesta1 = Entry(self.miFrame, state='readonly')
        self.entryTkRespuesta1['font'] = self.myFont2
        self.entryTkRespuesta1.place(x=90, y=480, width=600, height=50)

        self.entryTkRespuesta2 = Entry(self.miFrame, state='readonly')
        self.entryTkRespuesta2['font'] = self.myFont2
        self.entryTkRespuesta2.place(x=90, y=540, width=600, height=50)

        self.entryErrorLexico= Entry(self.miFrame, state='readonly')
        self.entryErrorLexico['font'] = self.myFont2
        self.entryErrorLexico.place(x=720, y=180, width=200, height=110)

        self.entryErrorSintactico= Entry(self.miFrame, state='readonly')
        self.entryErrorSintactico['font'] = self.myFont2
        self.entryErrorSintactico.place(x=720, y=360, width=200, height=110)

        self.label2 = Label(self.miFrame, background="#FFF")
        self.label2.place(x=90, y=670, width=800, height=5)

        self.boton6 = Button(self.miFrame, text="Cargar \nPreguntas", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0, command= lambda: self.leer())
        self.boton6['font']=self.myFont
        self.boton6.place(x=90, y=640, width=150, height=60)
        self.boton4 = Button(self.miFrame, text="Cargar \nRespuestas", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        self.boton4['font']=self.myFont
        self.boton4.place(x=430, y=640, width=150, height=60)
        self.boton5 = Button(self.miFrame, text="Cargar \nT Simbolos", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0)
        self.boton5['font']=self.myFont
        self.boton5.place(x=770, y=640, width=150, height=60)

        self.label3 = Label(self.miFrame, background="#1B2631", text="O", foreground="#FFF")
        self.label3['font']=self.myFont2
        self.label3.place(x=40, y=130)

        self.label4 = Label(self.miFrame, background="#1B2631", text="Tk1", foreground="#FFF")
        self.label4['font']=self.myFont2
        self.label4.place(x=40, y=190)

        self.label11 = Label(self.miFrame, background="#1B2631", text="AL", foreground="#FFF")
        self.label11['font']=self.myFont2
        self.label11.place(x=40, y=250)

        self.label5 = Label(self.miFrame, background="#1B2631", text="Tk2", foreground="#FFF")
        self.label5['font']=self.myFont2
        self.label5.place(x=40, y=310)

        self.label6 = Label(self.miFrame, background="#1B2631", text="AS", foreground="#FFF")
        self.label6['font']=self.myFont2
        self.label6.place(x=40, y=370)

        self.label7 = Label(self.miFrame, background="#1B2631", text="Rp", foreground="#FFF")
        self.label7['font']=self.myFont2
        self.label7.place(x=40, y=430)

        self.label8 = Label(self.miFrame, background="#1B2631", text="Tk1", foreground="#FFF")
        self.label8['font']=self.myFont2
        self.label8.place(x=40, y=490)

        self.label9 = Label(self.miFrame, background="#1B2631", text="Tk2", foreground="#FFF")
        self.label9['font']=self.myFont2
        self.label9.place(x=40, y=550)

        self.label10 = Label(self.miFrame, background="#1B2631", text="Error Lexico", foreground="#FFF")
        self.label10['font']=self.myFont2
        self.label10.place(x=720, y=140)

        self.label10 = Label(self.miFrame, background="#1B2631", text="Error Sintactico", foreground="#FFF")
        self.label10['font']=self.myFont2
        self.label10.place(x=720, y=320)

    def leer(self):
        with open('preguntas.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                self.entryOracion.insert(0,''.join(row))



app = Tk()
window = Interface(app)
app.mainloop()