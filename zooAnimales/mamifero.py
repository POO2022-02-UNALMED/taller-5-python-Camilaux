from zooAnimales.animal import Animal

class Mamifero(Animal):

    _caballos = 0
    _leones = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__( nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls._caballos += 1
        cls._listado.append(Mamifero(nombre, edad, "pradera", genero, True, 4))
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(cls,nombre, edad, genero):
        cls.leones += 1
        cls._listado.append(Mamifero(nombre, edad, "selva", genero, True, 4))
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    def setPelaje(self,pelaje):
        self._pelaje = pelaje
    
    def getPelaje(self):
        return self._pelaje

    def setPatas(self,patas):
        self._patas = patas

    def getPatas(self):
        return self._patas
        
