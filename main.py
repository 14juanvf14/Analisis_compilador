class Afd:
    def __init__(self, cadena):
        self.cadena = cadena

    def automataId(self, caracter):
        self.estado=0
        for i in range(0, len(self.cadena)):
            self.transicion=self.cadena[i]
            if str.isalpha(self.transicion):
                self.estado=1
            elif self.estado==1 and  str.isalpha(self.transicion) or str.isdigit(self.transicion):
                self.estado=1
        if self.estado==1:
            return True
        else:
            return False

    def automataInt(self, caracter):
        self.estado=0
        for i in range(0, len(self.cadena)):
            self.transicion=self.cadena[i]
            if str.isdigit(self.transicion):
                self.estado=1
        if self.estado==1:
            return True
        else:
            return False
