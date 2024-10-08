import time
import sys
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

def escribir_poco_a_poco(texto="hola como estas", retraso=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()  # Asegura que se imprima el carácter inmediatamente
        time.sleep(retraso)  # Tiempo de retraso entre cada carácter
    print()  # Añade un salto de línea al final

def iniciar_juego_desde_mapa(mapa):
    # Función para iniciar el juego con una instancia de mapa ya existente.
    print("Iniciando juego desde un mapa cargado...")
    juego = IniciarJuego()  # Crea una nueva instancia del juego
    juego.mapa = mapa        # Usa el mapa cargado en vez de uno nuevo
    juego.Acertijos.mapa = mapa  # Asegurarse de que el objeto acertijos también tenga el mapa actualizado
    juego.iniciar()          # Inicia el flujo del juego directamente

class main():
    while True:
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
            # Mostrar historia poco a poco
            escribir_poco_a_poco("Esta es la historia de Corona de Hielo...")

        elif opcion == "4":
            # Terminar ejecución del juego
            print("Gracias por jugar")
            sys.exit()

        else:
            print("Opción no válida. Inténtelo de nuevo.")
