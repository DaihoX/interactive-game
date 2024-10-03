from src.Mapa import Mapa


class IniciarJuego:
    def __init__(self):
        self.mapa = Mapa()

    def iniciar(self):
        print("Bienvenido a la aventura de habitaciones 3x3!")
        while True:
            self.mapa.mostrar_mapa()
            accion = input("¿Qué quieres hacer? (mover/resolver/salir): ").lower()

            if accion == "mover":
                direccion = input("¿En qué dirección? (arriba/abajo/izquierda/derecha): ").lower()
                self.mapa.mover(direccion)
            elif accion == "resolver":
                self.mapa.resolver_habitacion()
            elif accion == "salir":
                print("¡Gracias por jugar!")
                break
            else:
                print("Acción no válida")


if __name__ == "__main__":
    juego = Main()
    juego.iniciar()