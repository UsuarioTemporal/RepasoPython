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
# ficheroBinario = open("repaso9/listaNombre","rb") # read binary
ficheroPersonas = open("repaso9/lasPersonas","rb")
# lists = pickle.load(ficheroBinario)
listaPers = pickle.load(ficheroPersonas)
# print(lists)
print(listaPers)

ficheroPersonas.close()
# ficheroBinario.close()