class Usuario:
    #constructor
    def __init__(self, nombre, password):
        self.__nombre = nombre
        self.__password = password
    
    #retornar el empleado
    def info(self):
        return self.__nombre, self.__password
    