import pandas as pd

from Control.TokenAfd import TokenAfd


class Lexico:
    def __init__(self, cadenaTexto):
        self.cadenaTexto = str(cadenaTexto)
        self.tabla=[["Lexema", "token", "tipo", "constante"]]
        self.palabraError=""
    def analizador(self):
        self.list = self.cadenaTexto.split()
        for i in self.list:
            tokenit = TokenAfd(''.join(i))
            if tokenit.automataId():
                if ''.join(i)=='Pedro' or ''.join(i)=='Juan' or ''.join(i)=='medalla' or ''.join(i)=='futbol' or ''.join(i)=='ayer':
                    self.tabla.append([''.join(i), 'ID', 'SUST', 'SI'])
                elif ''.join(i)=='ha':
                    self.tabla.append([''.join(i), 'ID', 'MODAL', ' '])
                elif ''.join(i)=='una':
                    self.tabla.append([''.join(i), 'ID', 'DET', ' '])
                elif ''.join(i)=='jugado' or ''.join(i)=='ganado' or ''.join(i)=='gano':
                    self.tabla.append([''.join(i), 'ID', 'VERB', 'SI'])
                else:
                    self.tabla.append([''.join(i), 'ID', 'ID', ' '])
            elif tokenit.automataInt():
                    self.tabla.append([''.join(i), 'INT', 'DET', ''.join(i)])
            elif tokenit.automataPa():
                    self.tabla.append([''.join(i), '¿', ' ', ' '])
            elif tokenit.automataPc():
                    self.tabla.append([''.join(i), '?', ' ', ' '])
            elif tokenit.estado == 99:
                self.palabraError=''.join(i)
                break
        if tokenit.estado == 99:
            return False
        else:
            return True
