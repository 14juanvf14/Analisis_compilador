import numpy as np

class TablaSimbolo:
    def __init__(self, tabla):
        self.tabla = tabla

    def generarTabla(self):
        np.savetxt("../Model/tabla_Simbolos.csv", self.tabla, delimiter =",",fmt ='% s')