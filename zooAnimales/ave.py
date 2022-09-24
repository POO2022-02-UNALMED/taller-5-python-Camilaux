from zooAnimales.animal import Animal

class Ave(Animal):

    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__( nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls,nombre, edad, genero):
        cls.halcones += 1
        cls._listado.append(Ave(nombre, edad, "montanas", genero, "cafe glorioso"))
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls,nombre, edad, genero):
        cls.aguilas += 1
        cls._listado.append(Ave(nombre, edad, "montanas", genero, "blanco y amarillo"))
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    def setColorPlumas(self,color):
        self._colorPlumas = color
    
    def getColorPlumas(self):
        return self._colorPlumas


    