from zooAnimales.animal import Animal

class Pez(Animal):

    salmones = 0
    bacalaos =  0  
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, color, aletas):
        super().__init__( nombre, edad, habitat, genero)
        self._colorEscamas = color
        self._cantidadAletas = aletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls,nombre, edad, genero):
        cls.salmones += 1
        cls._listado.append(Pez(nombre, edad, "oceano", genero, "rojo", 6))
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls,nombre, edad, genero):
        cls.bacalaos += 1
        cls._listado.append(Pez(nombre, edad, "oceano", genero, "gris", 6))
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def setColorEscamas(self,color):
        self._colorEscamas = color
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self,aletas):
        self._cantidadAletas = aletas

    def getCantidadAletas(self):
        return self._cantidadAletas

    
