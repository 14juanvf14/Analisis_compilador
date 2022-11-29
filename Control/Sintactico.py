from csv import reader


class Sintax():
    t = ["SUST", "DET", "MODAL", "VERB"]
    nt = ["O", "SN", "SV", "FVERBAL", "AUX"]

    def __init__(self, cadena, listar):
        self.list=listar
        self.cadena = cadena.split()
        self.pila=["$","O"]
        self.palabraError=0


    def analiza(self):
        for i in range(0,len(self.cadena)):
            if self.isTerminal(self.pila[-1]) or self.pila[-1]=='$':
                if self.pila[-1] == self.cadena[i]:
                    self.pila.pop()
                else:
                    self.palabraError=i
                    break
            else:
                if self.m(self.pila[-1],self.cadena[i]):
                    pass
                else:
                    self.palabraError=i
                    break
        if self.pila[-1] == '$':
            return True
        else:
            return False

    def m(self, a,b):
        if b == 'ID':
            return False
        else:
            a2 = self.nt.index(a)
            b2 = self.t.index(b)
            if self.list[a2][b2] != '':
                self.pila.pop()
                listaAux=self.list[a2][b2]
                for i in range(0,len(listaAux)):
                    self.pila.append(listaAux[0][i])
                return True
            else:
                return False



    def isTerminal(self, s):
        return s in self.t

    def isNonTerminal(self, s):
        return s in self.nt
