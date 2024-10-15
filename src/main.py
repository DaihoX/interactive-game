import sys
import webbrowser
from Partida import Partida
from Mapa import Mapa
from IniciarJuego import IniciarJuego


def mostrar_menu():
    print("\n--- Bienvenido a Corona de Hielo---")
    print("Corona de Hielo es una aventura interactiva de puzzles")
    print("1. Iniciar una nueva partida")
    print("2. Cargar partida")
    print("3. Historia")
    print("4. Salir")


def iniciar_juego_desde_mapa(mapa):
    # Función para iniciar el juego con una instancia de mapa ya existente.
    print("Iniciando juego desde un mapa cargado...")
    juego = IniciarJuego()  # Crea una nueva instancia del juego
    juego.mapa = mapa  # Usa el mapa cargado en vez de uno nuevo
    juego.Acertijos.mapa = mapa  # Asegurarse de que el objeto acertijos también tenga el mapa actualizado
    juego.iniciar()  # Inicia el flujo del juego directamente


class main():
    while True:
        # Muestra el menú principal y espera la elección del usuario para continuar
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            # Iniciar nueva partida
            print("Iniciando nueva partida...")
            mapa = Mapa()  # Crear una nueva instancia del mapa (estado nuevo del juego)
            # mapa.mostrar_mapa()  # Mostrar el mapa inicial
            IniciarJuego().iniciar()

        elif opcion == "2":
            # Cargar una partida de los 3 slots de guardado
            slot = input("Seleccione el slot para cargar la partida (1, 2 o 3): ")
            if slot in ["1", "2", "3"]:
                archivo_guardado = f"partida_slot_{slot}.pkl"
                partida = Partida(archivo=archivo_guardado)
                mapa = partida.cargar()  # Intentamos cargar la partida
                if mapa:
                    # mapa.mostrar_mapa()  # Mostrar el estado del mapa cargado
                    print(f"Partida del slot {slot} cargada con éxito")
                    iniciar_juego_desde_mapa(mapa)  # Iniciar el juego con el mapa cargado
                else:
                    print(f"No se pudo cargar la partida del slot {slot}")
            else:
                print("Slot no válido.")

        elif opcion == "3":
            # Mostrar historia redireccionado al reposotorio donde se aloja
            webbrowser.open("https://github.com/DaihoX/interactive-game/blob/main/historia.txt")

        elif opcion == "4":
            # Terminar ejecución del juego
            print("Gracias por jugar")
            sys.exit()

        else:
            # Cuando no se elige una opción válidam mostrar mensaje de error
            print("Opción no válida. Inténtelo de nuevo.")
