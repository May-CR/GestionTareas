from Model import Observer


class Notification(Observer):
    def actualizar(self, mensaje):
        print(f"🔔 Notificación: {mensaje}")