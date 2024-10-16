# Clase Habitacion para representar una habitación del mapa
class Habitacion:
    # Inicializa la habitación como no resuelta
    def __init__(self):
        self.resuelto = False

    # Método para resolver la habitación
    def resolver(self):
        self.resuelto = True
