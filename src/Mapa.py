import pickle  # Importar pickle para la serialización
from Habitacion import Habitacion
class Mapa:
    def __init__(self):
        # Crear un mapa 3x3 de habitaciones
        self.habitaciones = [[Habitacion() for _ in range(3)] for _ in range(3)]
        self.posicion_actual = (0, 0)

    def mostrar_mapa(self):
        for fila in range(3):
            fila_habitaciones = ''
            for columna in range(3):
                if self.posicion_actual == (fila, columna):
                    fila_habitaciones += '[P] '  # P para indicar la posición actual
                elif self.habitaciones[fila][columna].resuelto:
                    fila_habitaciones += '[R] '  # R para indicar habitación resuelta
                else:
                    fila_habitaciones += '[ ] '  # Habitación no resuelta
            print(fila_habitaciones)

    def mover(self, direccion):
        fila, columna = self.posicion_actual

        # Determinar la nueva posición basada en la dirección
        nueva_fila, nueva_columna = fila, columna
        if direccion == "arriba" and fila > 0:
            nueva_fila = fila - 1
        elif direccion == "abajo" and fila < 2:
            nueva_fila = fila + 1
        elif direccion == "izquierda" and columna > 0:
            nueva_columna = columna - 1
        elif direccion == "derecha" and columna < 2:
            nueva_columna = columna + 1
        else:
            print("Movimiento no válido")
            return

        # Verificar si la nueva habitación está resuelta o si la actual está resuelta (para moverte a adyacentes)
        if self.habitaciones[fila][columna].resuelto or self.habitaciones[nueva_fila][nueva_columna].resuelto:
            self.posicion_actual = (nueva_fila, nueva_columna)
            print(f"Te has movido a la habitación ({nueva_fila}, {nueva_columna})")
        else:
            print("¡Debes resolver la habitación actual antes de moverte a una adyacente!")

    def resolver_habitacion(self):
        fila, columna = self.posicion_actual
        self.habitaciones[fila][columna].resolver()
        print(f"Habitación en ({fila}, {columna}) resuelta")

    def guardar(self):
        """Método para guardar el estado del mapa en un archivo."""
        with open('mapa_guardado.pkl', 'wb') as f:
            pickle.dump(self, f)  # Serializa la instancia de Mapa

    @staticmethod
    def cargar():
        """Método para cargar el estado del mapa desde un archivo."""
        try:
            with open('mapa_guardado.pkl', 'rb') as f:
                return pickle.load(f)  # Deserializa la instancia de Mapa
        except (FileNotFoundError, EOFError):
            print("No hay un archivo de mapa guardado.")
            return None
