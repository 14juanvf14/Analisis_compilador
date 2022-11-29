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
                if ''.join(i)=='Pedro' or ''.join(i)=='Juan':
                    self.tabla.append([''.join(i), 'ID', 'SUST', 'SI'])
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
