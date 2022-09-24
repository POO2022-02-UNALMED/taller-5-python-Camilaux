from zooAnimales.animal import Animal

class Reptil(Animal):

    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, color, largo):
        super().__init__( nombre, edad, habitat, genero)
        self._colorEscamas = color
        self._largoCola = largo
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        return "tierra"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        cls._listado.append(Reptil(nombre, edad, "humedal", genero, "verde", 3))
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        cls._listado.append(Reptil(nombre, edad, "jungla", genero, "blanco", 1))
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    def setColorEscamas(self,color):
        self._colorEscamas = color

    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self,cola):
        self._largoCola = cola

    def getLargoCola(self):
        return self._largoCola



    