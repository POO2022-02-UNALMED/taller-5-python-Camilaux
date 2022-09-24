class Zoologico:
    def __init__(self,nombre,ubicacion,zona):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = [zona]

    def agregarZonas(self,zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        return len(self._zonas)

    def setNombre(self,nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre 

    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion

    def getUbicacion(self):
        return self._ubicacion
    
    def getZonas(self):
        return self._zonas