from src.Personaje import Personaje


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
    elif jefeFinal.esta_vivo():
        print("\nHa ganado", jefeFinal.nombre)
    else:
        print("\nEmpate")


jefeFinal = Personaje("Jefe Final", 10, 10, 10, 100)
jugador = Personaje("Jugador", 5, 5, 5, 50)

combate(jugador, jefeFinal)

