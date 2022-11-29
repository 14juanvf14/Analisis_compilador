from csv import reader


class Sintax():
    t = ["SUST", "DET", "MODAL", "VERB"]
    nt = ["O", "SN", "SV", "FVERBAL", "AUX"]

    def __init__(self, cadena, list):
        self.list=list
        self.cadena = cadena.split()
        self.pila=["$","O"]
        self.palabraError=0


    def analiza(self):
        for i in range(0,len(self.cadena)):
            if self.isTerminal(self.pila[-1]) or self.cadena[i]=='$':
                if self.pila[-1] == self.cadena[i]:
                    self.pila.pop()
                else:
                    self.palabraError=i
                    break
            else:
                if self.m(self.pila[-1],self.cadena):
                    pass
                else:
                    break
        if self.pila[-1] == '$':

    def m(self, a,b):
        a2 = self.nt.index(a)
        b2 = self.t.index(b)
        if self.list[a2][b2] != '':
            self.pila.pop()
            listaAux=self.list[a2][b2]
            for i in range(len(listaAux),0,-1):
                self.pila.append(listaAux[i])
            return True
        else:
            return False



    def isTerminal(self, s):
        return s in self.t

    def isNonTerminal(self, s):
        return s in self.nt
