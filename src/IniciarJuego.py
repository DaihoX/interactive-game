import Mapa
from Acertijos import Acertijos
from Partida import Partida
from Personaje import Personaje
from combate import combate


class IniciarJuego:

    jefeFinal = Personaje("Jefe Final", 10, 10, 10, 100)
    jugador = Personaje("Jugador", 5, 5, 5, 50)

    def __init__(self, mapa=None):
        if mapa is None:
            self.mapa = Mapa.Mapa()  # Si no hay un mapa cargado, se crea uno nuevo
        else:
            self.mapa = mapa  # Usamos el mapa cargado si está disponible
        self.Acertijos = Acertijos(self.mapa)

    def iniciar(self):
        print("¡Bienvenido a la aventura de habitaciones 3x3!")
        while True:
            self.mapa.mostrar_mapa()
            accion = input("¿Qué quieres hacer? (mover/resolver/pelear contra el jefe/salir/guardar partida): ").lower()

            if accion == "mover":
                direccion = input("¿En qué dirección? (arriba/abajo/izquierda/derecha): ").lower()
                self.mapa.mover(direccion)
            elif accion == "resolver":
                if self.Acertijos.iniciar_pregunta():
                    break
            elif accion == "salir":
                print("¡Gracias por jugar!")
                break  # Salir del ciclo si se completaron todos los acertijos
            elif accion == "guardar partida":
                # Guardar la partida en uno de los slots
                slot = input("Seleccione un slot para guardar la partida (1, 2 o 3): ")
                if slot in ["1", "2", "3"]:
                    archivo_guardado = f"partida_slot_{slot}.pkl"
                    partida = Partida(archivo=archivo_guardado)
                    partida.guardar(self.mapa)  # Guardamos el estado del mapa en el slot elegido
                    print(f"Partida guardada en el slot {slot}")
                else:
                    print("Slot no válido. No se guardó la partida.")
            elif accion == "pelear contra el jefe":
                combate(IniciarJuego.jugador, IniciarJuego.jefeFinal)
                break
            else:
                print("Acción no válida")
