import json
import User_Profile as UP
from User_Profile import User

class JSONManager:
    def __init__(self, archivo):
        self.archivo = archivo

        
        
    def guardar_lista(self, lista_objetos):
        try:
            with open(self.archivo, 'w') as f:
                json.dump([vars(objeto) for objeto in lista_objetos], f)
            print("Lista de objetos guardada correctamente en", self.archivo)
        except Exception as e:
            print("Error al guardar la lista de objetos:", str(e))

    def cargar_lista(self, clase):
        try:
            with open(self.archivo, 'r') as f:
                data = json.load(f)
                return [clase(**item) for item in data]
        except Exception as e:
            print("Error al cargar la lista de objetos:", str(e))
            return []

