from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio

class Animal:
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []

    def movimiento(self):
        return "desplazarse"
        

    def totalPorTipo(self):
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\nAves: " + Ave.cantidadAves() + "\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() + "\nAnfibios: " + Anfibio.cantidadAnfibios()

    @classmethod
    def setTotalAnimales(cls,total):
        cls.totalAnimales = total
    
    @classmethod
    def getTotalAnimales(cls):
        return cls.totalAnimales

    def setNombre(self,nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setEdad(self,edad):
        self._edad = edad
    
    def getEdad(self):
        return self._edad

    def setHabitat(self,habitat):
        self._habitat = habitat

    def getHabitat(self):
        return self._habitat

    def setGenero(self,genero):
        self._genero = genero

    def getGenero(self):
        return self._genero

    def getZona(self):
        return self._zona

    def __str__(self):
        if self.len(self.getZona()) != 0:
            cadena = "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self.getZona() + ", en el " + self.getNombre()
        else:
            cadena = "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
        return cadena