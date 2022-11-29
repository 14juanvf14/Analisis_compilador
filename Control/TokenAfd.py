class TokenAfd:
    def __init__(self, cadena):
        self.cadena = cadena
        self.caracter = ""

    def automataId(self):
        self.estado = 0
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == 0 and str.isalpha(self.transicion):
                self.estado = 1
            elif self.estado == 1 and str.isalpha(self.transicion) or self.estado == 1 and str.isdigit(self.transicion):
                self.estado = 1
            else:
                self.estado = 99
                self.caracter = self.transicion

        if self.estado == 1:
            return True
        else:
            return False

    def automataInt(self):
        self.estado = 0
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if str.isdigit(self.transicion):
                self.estado = 1
            else:
                self.estado = 99
                self.caracter = self.transicion

        if self.estado == 1:
            return True
        else:
            return False

    def automataPa(self):
        self.estado = 0
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == 0 and self.transicion == '¿':
                self.estado = 1
            else:
                self.estado = 99
                self.caracter = self.transicion
        if self.estado == 1:
            return True
        else:
            return False

    def automataPc(self):
        self.estado = 0
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == 0 and self.transicion == '?':
                self.estado = 1
            else:
                self.estado = 99
                self.caracter = self.transicion
        if self.estado == 1:
            return True
        else:
            return False