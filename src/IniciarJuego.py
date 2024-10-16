import Mapa
from Acertijos import Acertijos
from Partida import Partida
from Personaje import Personaje
from combate import combate

# Clase para iniciar el juego y manejar las interacciones con el usuario
class IniciarJuego:

    # Crear un jefe final con 100 de vida y 10 de fuerza y defensa
    jefeFinal = Personaje("Alastor", 10, 10, 10, 100)
    # Crear un jugador con 5 de vida, fuerza y defensa
    jugador = Personaje("Daiho", 5, 5, 5, 50)

    # Constructor de la clase
    def __init__(self, mapa=None):
        # Crear un nuevo mapa si no se proporciona uno
        if mapa is None:
            self.mapa = Mapa.Mapa()  # Si no hay un mapa cargado, se crea uno nuevo

        # Si se proporciona un mapa, se usa ese mapa
        else:
            self.mapa = mapa  # Usamos el mapa cargado si está disponible

        # Crear una instancia de acertijos
        self.Acertijos = Acertijos(self.mapa)

    # Método para iniciar el juego
    def iniciar(self):

        print("¡Bienvenido a la aventura de habitaciones 3x3!")

        # Mientras el jugador no haya completado todos los acertijos que siga el bucle del juego
        while True:

            # Mostrar el mapa actual
            self.mapa.mostrar_mapa()
            accion = input("¿Qué quieres hacer? "
                           "( mover/ resolver / pelear (Pelea contra el jefe final/ estadisticas / guardar partida)"
                           "/ salir ): ").lower()

            # Realizar la acción seleccionada por el jugador
            if accion == "mover":
                direccion = input("¿En qué dirección? (arriba/abajo/izquierda/derecha): ").lower()
                self.mapa.mover(direccion)

            # Resolver el acertijo en la habitación actual
            elif accion == "resolver":
                if self.Acertijos.iniciar_pregunta():
                    break

            # Salir del juego
            elif accion == "salir":
                print("¡Gracias por jugar!")
                break  # Salir del ciclo si se completaron todos los acertijos

            # Guardar la partida actual
            elif accion == "guardar partida":
                # Guardar la partida en uno de los slots
                slot = input("Seleccione un slot para guardar la partida (1, 2 o 3): ")

                # Verificar si el slot seleccionado es válido
                if slot in ["1", "2", "3"]:
                    # Crear un archivo con el nombre del slot seleccionado
                    archivo_guardado = f"partida_slot_{slot}.pkl"
                    partida = Partida(archivo=archivo_guardado)
                    
                    # Guardamos el estado del mapa y los acertijos en el slot elegido
                    partida.guardar(self.mapa, self.Acertijos)
                    print(f"Partida guardada en el slot {slot}")  # Muestra el slot en el que guardamos la partida

                # Si el slot no es válido, mostrar un mensaje de error
                else:
                    print("Slot no válido. No se guardó la partida.")

            # Opcion para pelear antes con el boss         
            elif accion == "pelear":
                combate(IniciarJuego.jugador, IniciarJuego.jefeFinal)
                break
            # Muestra las estadisticas actuales del jugador 
            elif accion == "estadisticas":
                print(" Vida: " + str(IniciarJuego.jugador.vida) +
                      " Fuerza: " + str(IniciarJuego.jugador.fuerza) +
                      " Defensa: " + str(IniciarJuego.jugador.defensa))
            # Si la acción no es válida, mostrar un mensaje de error
            else:
                print("Acción no válida")
