import pickle  # Importar pickle para la serialización
from Habitacion import Habitacion
from combate import combate
from IniciarJuego import IniciarJuego

# Creanis la clase mapa la cual va a contener las habitaciones y las interacciones de las mismas
class Mapa:
    # Constructor de la clase
    def __init__(self):

        # Crear un mapa 3x3 de habitaciones
        self.habitaciones = [[Habitacion() for _ in range(3)] for _ in range(3)]
        self.posicion_actual = (0, 0)

    # Método para mostrar el mapa
    def mostrar_mapa(self):

        # Mostrar el mapa con la posición actual y las habitaciones resueltas
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

    # Método para moverse a una habitación adyacente
    def mover(self, direccion):

        # Obtener la fila y columna de la posición actual
        fila, columna = self.posicion_actual
        # Determinar la nueva posición basada en la dirección
        nueva_fila, nueva_columna = fila, columna

        # Verificar si la dirección es válida y actualizar la nueva fila y columna
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

        # Si la habitación actual no está resuelta y la adyacente tampoco, mostrar mensaje
        else:
            print("¡Debes resolver la habitación actual antes de moverte a una adyacente!")

    # Método para resolver la habitación actual
    def resolver_habitacion(self):

        # Obtener la fila y columna de la posición actual
        fila, columna = self.posicion_actual
        self.habitaciones[fila][columna].resolver()
        print(f"Habitación en ({fila}, {columna}) resuelta")

        # Verificar si todas las habitaciones están resueltas
        if self.todas_habitaciones_resueltas():
            print("¡Felicidades! Has completado todos los acertijos. La aventura ha finalizado.")
            print("Ahora puedes combatir el jefe final")

            # Iniciar combate contra el jefe final cuando todas las habitaciones estén resueltas
            combate(IniciarJuego.jugador, IniciarJuego.jefeFinal)
            return True  # Retorna True si todas las habitaciones están resueltas

        return False  # Retorna False si aún hay habitaciones no resuelta

    # Método para guardar el estado del mapa en un archivo
    def guardar(self):

        # Serializar el estado del mapa en un archivo
        with open('mapa_guardado.pkl', 'wb') as f:
            pickle.dump(self, f)

    # Método para cargar el estado del mapa desde un archivo
    @staticmethod
    def cargar():
       # Deserializar el estado del mapa desde un archivo
        try:
            with open('mapa_guardado.pkl', 'rb') as f:
                return pickle.load(f)  # Deserializa la instancia de Mapa

        except (FileNotFoundError, EOFError):
            print("No hay un archivo de mapa guardado.")
            return None

    # Método para verificar si todas las habitaciones están resueltas
    def todas_habitaciones_resueltas(self):

        # Verificar si todas las habitaciones están resueltas
        for fila in self.habitaciones:

            # Verificar cada habitación en la fila
            for habitacion in fila:

                if not habitacion.resuelto:
                    return False

        return True
