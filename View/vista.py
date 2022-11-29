import tkinter
from tkinter import *
from tkinter import font as font
from Control.Lexico import Lexico
from Control.Sintactico import Sintax
from Model.TablaAS import Primerosiguiente
from Model.TablaSimbolos import TablaSimbolo as ts
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

        self.boton1 = Button(self.miFrame, text="Analisis \nLexico", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0, command= lambda: self.lexico())
        self.boton1['font']=self.myFont
        self.boton1.place(x=90, y=20, width=150, height=60)
        self.boton2 = Button(self.miFrame, text="Analisis \nSintactico", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0, command= lambda: self.sintactico())
        self.boton2['font']=self.myFont
        self.boton2.place(x=430, y=20, width=150, height=60)
        self.boton3 = Button(self.miFrame, text="Generar \nrespuesta", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0, command= lambda: self.respuesta())
        self.boton3['font']=self.myFont
        self.boton3.place(x=770, y=20, width=150, height=60)

        self.entryOracion = Entry(self.miFrame)
        self.entryOracion['font'] = self.myFont2
        self.entryOracion.place(x=90, y=120, width=600, height=50)

        self.entryTkLexico1 = Entry(self.miFrame)
        self.entryTkLexico1['font'] = self.myFont2
        self.entryTkLexico1.place(x=90, y=180, width=600, height=50)

        self.entryTkLexicoConfirma = Entry(self.miFrame)
        self.entryTkLexicoConfirma['font'] = self.myFont2
        self.entryTkLexicoConfirma.place(x=90, y=240, width=600, height=50)

        self.entryTkLexico2 = Entry(self.miFrame)
        self.entryTkLexico2['font'] = self.myFont2
        self.entryTkLexico2.place(x=90, y=300, width=600, height=50)

        self.entrySintactico = Entry(self.miFrame)
        self.entrySintactico['font'] = self.myFont2
        self.entrySintactico.place(x=90, y=360, width=600, height=50)

        self.entryRespuesta = Entry(self.miFrame)
        self.entryRespuesta['font'] = self.myFont2
        self.entryRespuesta.place(x=90, y=420, width=600, height=50)

        self.entryTkRespuesta1 = Entry(self.miFrame)
        self.entryTkRespuesta1['font'] = self.myFont2
        self.entryTkRespuesta1.place(x=90, y=480, width=600, height=50)

        self.entryTkRespuesta2 = Entry(self.miFrame)
        self.entryTkRespuesta2['font'] = self.myFont2
        self.entryTkRespuesta2.place(x=90, y=540, width=600, height=50)

        self.entryErrorLexico= Entry(self.miFrame)
        self.entryErrorLexico['font'] = self.myFont2
        self.entryErrorLexico.place(x=720, y=180, width=200, height=110)

        self.entryErrorSintactico= Entry(self.miFrame)
        self.entryErrorSintactico['font'] = self.myFont2
        self.entryErrorSintactico.place(x=720, y=360, width=200, height=110)

        self.label2 = Label(self.miFrame, background="#FFF")
        self.label2.place(x=90, y=670, width=800, height=5)

        self.boton6 = Button(self.miFrame, text="Cargar \nPreguntas", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0, command= lambda: self.leer())
        self.boton6['font']=self.myFont
        self.boton6.place(x=90, y=640, width=150, height=60)
        self.boton4 = Button(self.miFrame, text="Cargar \nRespuestas", activebackground="#006EB8", activeforeground="#FFF", background="#015289", foreground="#FFF", border=0, command= lambda: self.cargaRespuesta())
        self.boton4['font']=self.myFont
        self.boton4.place(x=770, y=640, width=150, height=60)

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
        with open('../Model/preguntas.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                self.entryOracion.delete(0,"end")
                self.entryOracion.insert(0,''.join(row))
    def lexico(self):
        analizador = Lexico(self.entryOracion.get())

        self.tk1=""
        self.tk2=""

        self.entryTkLexico1.delete(0,"end")
        self.entryTkLexico2.delete(0,"end")
        self.entryErrorLexico.delete(0, "end")
        self.entryTkLexicoConfirma.delete(0,"end")
        if analizador.analizador():
            self.entryTkLexicoConfirma.insert(0,"Analisis realizado correctamente")
            self.tabla = analizador.tabla
            for i in range(1, len(self.tabla)):
                self.tk1 = self.tk1 + self.tabla[i][1] + " "
                self.tk2 = self.tk2 + self.tabla[i][2] + " "
            self.entryTkLexico1.insert(0,self.tk1)
            self.entryTkLexico2.insert(0,self.tk2)
            tabla = ts(self.tabla)
            tabla.generarTabla()

        else:
            self.entryTkLexicoConfirma.insert(0,"Hay un error en el analisis")
            self.tabla = analizador.tabla
            for i in range(1, len(self.tabla)):
                self.tk1 = self.tk1 + self.tabla[i][1] + " "
                self.tk2 = self.tk2 + self.tabla[i][2] + " "
            self.entryTkLexico1.insert(0,self.tk1)
            self.entryTkLexico2.insert(0,self.tk2)
            self.entryErrorLexico.insert(0,"Palabra "+analizador.palabraError)

    def sintactico(self):
        self.entrySintactico.delete(0, "end")
        self.entryErrorSintactico.delete(0, "end")
        primero = Primerosiguiente()
        primero.main()
        self.listica = primero.list
        segundo = Sintax(self.tk2, self.listica)
        if(segundo.analiza()):
            self.entrySintactico.insert(0,"Analisis sintactico correcto")
        else:
            self.entrySintactico.insert(0,"Analisis sintactico con error")
            self.entryErrorSintactico.insert(0,self.tabla[segundo.palabraError+1][0])

    def cargaRespuesta(self):
        self.respuestas=[]
        with open('../Model/respuestas.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                self.respuestas.append("".join(row))
    def respuesta(self):

        self.entryRespuesta.delete(0,"end")

        if self.entryOracion.get() == '¿ Pedro ha ganado una medalla ?':
            self.entryRespuesta.insert(0, self.respuestas[0])
        elif self.entryOracion.get() == '¿ Juan ha jugado futbol ?':
            self.entryRespuesta.insert(0, self.respuestas[1])
        else:
            self.entryRespuesta.insert(0, self.respuestas[0])

        analizador = Lexico( self.entryRespuesta.get())
        self.tk3=""
        self.tk4=""

        self.entryTkRespuesta1.delete(0,"end")
        self.entryTkRespuesta2.delete(0,"end")

        if analizador.analizador():
            for i in range(1, len(self.tabla)):
                self.tk3 = self.tk3 + self.tabla[i][1] + " "
                self.tk4 = self.tk4 + self.tabla[i][2] + " "
            self.entryTkRespuesta1.insert(0,self.tk3)
            self.entryTkRespuesta2.insert(0,self.tk4)



app = Tk()
window = Interface(app)
app.mainloop()