class Sujeto:
    def __init__(self):
        self._observadores = []

    def agregarObservador(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensaje):
        for obs in self._observadores:
            obs.actualizar(mensaje)