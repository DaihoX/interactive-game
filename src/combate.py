import sys
import time


# Función para iniciar el combate entre el jugador y el jefe final
def combate(jugador, jefeFinal):

    # Inicializar el turno
    turno = 0

    # Mientras el jugador y el jefe final estén vivos, se
    while jugador.esta_vivo() and jefeFinal.esta_vivo():
        # Mostrar el turno actual
        print("\nTurno", turno)
        # Realizar la acción del jugador y del jefe final
        print(">>> Acción de ", jugador.nombre, ":", sep="")
        jugador.atacar(jefeFinal)
        print(">>> Acción de ", jefeFinal.nombre, ":", sep="")
        jefeFinal.atacar(jugador)
        # Incrementar el turno
        turno = turno + 1
        # Esperar 1.5 segundos antes de continuar
        time.sleep(1.5)

    # Verificar si el jugador o el jefe final han ganado
    if jugador.esta_vivo():
        print("\nHa ganado", jugador.nombre)
        print("¡¡Felicidades!!, has completado Corona de Hierro"
              "Muchas gracias por jugar esta aventura de puzzles interactiva.")
        sys.exit()

    elif jefeFinal.esta_vivo():
        print("\nHa ganado", jefeFinal.nombre)
        print("Has perdido en la aventura, ¡Resuelve a las habitaciones para equiparte y vencer al jefe final!")

    # En caso de empate
    else:
        print("\nEmpate")
        print("Has perdido en la aventura, ¡Resuelve a las habitaciones para equiparte y vencer al jefe final!")