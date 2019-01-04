import pickle

class Persona(): 
    def __init__(self,nombre):
        self.__nombre=nombre
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,value):
        self.__nombre=value
    def mostrarDatos(self):
        print(self.__nombre)

thom = Persona("Thom")
carlos = Persona("Carlos")


personas = [thom,carlos]

fichero = open("repaso9/lasPersonas","wb")
pickle.dump(personas,fichero)

fichero.close()
del (fichero)