from Model import SingleTask
from Model import RecurringTask


class TaskFactory:
    @staticmethod
    def crearTarea(tipo, *args):
        if tipo == "unica":
            return SingleTask(*args)
        elif tipo == "recurrente":
            return RecurringTask(*args)
        else:
            raise ValueError("Tipo de tarea no válido")
