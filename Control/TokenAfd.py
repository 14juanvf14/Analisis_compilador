class TokenAfd:
    def __init__(self, cadena):
        self.cadena = cadena

    def automataId(self):
        self.estado = 0
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if str.isalpha(self.transicion):
                self.estado = 1
            elif self.estado == 1 and str.isalpha(self.transicion) or self.estado == 1 and str.isdigit(self.transicion):
                self.estado = 1
            else:
                self.estado = 99
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
        if self.estado == 1:
            return True
        else:
            return False
