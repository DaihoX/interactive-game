import sys


def combate(jugador, jefeFinal):
    turno = 0

    while jugador.esta_vivo() and jefeFinal.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador.nombre, ":", sep="")
        jugador.atacar(jefeFinal)
        print(">>> Acción de ", jefeFinal.nombre, ":", sep="")
        jefeFinal.atacar(jugador)
        turno = turno + 1
    if jugador.esta_vivo():
        print("\nHa ganado", jugador.nombre)
        print("¡¡Felicidades!!, has completado Corona de Hierro"
              "Muchas gracias por jugar esta aventura de puzzles interactiva.")
        sys.exit()
    elif jefeFinal.esta_vivo():
        print("\nHa ganado", jefeFinal.nombre)
        print("Has perdido en la aventura, ¡Resuelve a las habitaciones para equiparte y vencer al jefe final!")
    else:
        print("\nEmpate")


