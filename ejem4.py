class BasicCommand():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def getMarca(self):
        return self.marca


class Moto(BasicCommand):
    def acelerar(self, marca, modelo):
        super().__init__(self, marca, modelo)

    def getResultado(self):
        return self.getMarca()+" "+self.getModelo()

moto=Moto("KAWASSAKI","NINJA")
print(moto.getResultado())