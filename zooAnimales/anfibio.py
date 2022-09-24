from zooAnimales.animal import Animal

class Anfibio(Animal):

    _ranas = 0
    _salamandras = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, color, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = color
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "arrastar"

    @classmethod
    def crearRana(cls,nombre, edad, genero):
        cls.ranas += 1
        cls._listado.append(Anfibio(nombre, edad, "selva", genero, "rojo", True))
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls,nombre, edad, genero):
        cls.salamandras += 1
        cls._listado.append(Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False))
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    def setColorPiel(self,color):
        self._colorPiel = color

    def getColorPiel(self):
        return self._colorPiel

    def setVenenoso(self,venenoso):
        self._venenoso = venenoso

    def getVenenoso(self):
        return self._venenoso