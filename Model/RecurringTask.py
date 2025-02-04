class RecurringTask(task):
    def __init__(self, titulo, prioridad, fechaCulminacion , categoria, estado, idUser, frecuencia):
        super().__init__(titulo, prioridad, fechaCulminacion , categoria, estado, idUser)
        self.frecuencia = frecuencia