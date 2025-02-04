class Task:

    #constructor
    def __init__(self, titulo, prioridad, fechaCulminacion , categoria, estado, idUser):
        self.__titulo = titulo
        self.__prioridad = prioridad
        self.__fechaCulminacion = fechaCulminacion
        self.__categoria = categoria
        self.__estado = estado
        self.__idUser = idUser
    
    #retornar el empleado
    def info(self):
        return self.__titulo, self.__prioridad, self.__fechaCulminacion, self.__categoria, self.__estado, self.__idUser
    