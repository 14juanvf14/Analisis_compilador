import numpy as np
class Primerosiguiente():


    t = ["SUST","DET","MODAL","VERB"]
    nt = ["O","SN","SV","FVERBAL","AUX"]
    grammar = {
        "O":[["SN","SV"]],
        "SN":[["SUST"],["DET","SUST"]],
        "SV":[["AUX","FVERBAL"]],
        "FVERBAL":[["VERB"],["VERB","SN"]],
        "AUX":[["MODAL"]]
    }
    def __init__(self):
        self.list=[[[],[],[],[]],
                   [[],[],[],[]],
                   [[],[],[],[]],
                   [[],[],[],[]],
                   [[],[],[],[]]]
        self.listaFist= {}
        self.listFollow={}

    def isTerminal(self,s):
        return s in self.t

    def isNonTerminal(self, s):
        return s in self.nt

    def findSymbol(self,s):
        results = {}
        for nont in self.grammar:#Por NT de la gramatica
            for production in self.grammar[nont]:#Por produccion del simbolo
                for symbol in production:
                    if s in production:
                        try:
                            results[nont]+=[production]
                        except KeyError:
                            results[nont]=[production]
        return results

    #Funcion para los primeros de un NT
    def first(self, s):
        firsts = []
        for production in self.grammar[s]:#Para cada produccion de la regla
            #print("Analizamos la produccion "+str(production))
            if(self.isTerminal(production[0])):
                #print(production[0]+" es terminal")
                firsts.append(production[0])
            elif(self.isNonTerminal(production[0])):
                #print(production[0]+" es no terminal")
                firsts+=self.first(production[0])
        return firsts

    def follow(self, s):
        follows = []
        if s == next(iter(self.grammar)):#Si el NT es el estado inicial, el siguiente sera $
            follows.append("$")
        found = self.findSymbol(s)#Buscamos las producciones donde se encuentra nuestro NT
        for nont in found:#Por cada NT de las reglas encontradas
            for production in found[nont]:
                if(production.index(s) < len(production)-1):
                    nxt = production[production.index(s)+1]#El simbolo despues del NT
                    if(self.isTerminal(nxt)):#Si el simbolo es terminal
                        follows.append(nxt)#Agregamos ese simbolo a la lista de siguientes
                    elif(self.isNonTerminal(nxt)):#Si el simbolo es no terminal
                        nxt = self.first(nxt)#Buscamos los primeros del siguiente
                        if("e" in nxt):#Si existe epsilon en los primeros
                            nxt += self.follow(nont)#Se añaden los siguientes del padre
                        follows+= nxt
                else:
                    if(s != nont):
                        follows = self.follow(nont)
        follows = list(set(follows))
        if("e" in follows):
            follows.remove("e")
        return follows

    def printGrammar(self):
        for rule in self.grammar:#Por regla
            str_rule = rule + " -> "
            for production in self.grammar[rule]:#Por produccion del no terminal
                for symbol in production:#Por simbolo en la produccion
                    str_rule+=symbol
                str_rule+="|"
            str_rule = str_rule[:-1]
            print(str_rule)

    def printFirsts(self):
        print("Primeros:")
        for nont in self.nt:
            self.listaFist[nont]=self.first(nont)

    def printFollows(self):
        print("Siguientes:")
        for nont in self.nt:
            self.listFollow[nont]=self.follow(nont)



    def main(self):
        print("\nPrimeros y Siguientes de una gramatica\n")
        self.printGrammar()
        self.printFirsts()
        print(self.listaFist)
        self.printFollows()
        print(self.listFollow)
        self.tabla()

    def tabla(self):

        for nont in self.nt:
            for nont2 in self.t:
                if nont2 in self.listaFist[nont]:
                    a = self.nt.index(nont)
                    b = self.t.index(nont2)
                    self.list[a][b]=self.grammar[nont]
        np.savetxt("../Model/tabla_Sinta.csv", self.list, delimiter =";",fmt ='% s')


