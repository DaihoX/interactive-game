import IniciarJuego


class Acertijos:
    def __init__(self, mapa):
        self.Mapa = mapa
        # Separar los acertijos en tres categorías:
        self.acertijos_numericos = {
            "¿Cuánto es 5 + 5?": "10",
            "¿Cuánto es 12 * 12?": "144",
            "¿Cuánto es 15 / 3?": "5"
        }
        self.acertijos_cultura = {
            "¿Cuál es la capital de Francia?": "Paris",
            "¿Quién escribió 'Don Quijote'?": "Cervantes",
            "¿En qué año llegó el hombre a la Luna?": "1969"
        }
        self.acertijos_secuencia = {
            "¿Cuál es el siguiente número en la secuencia 2, 4, 8, 16, ...?": "32",
            "¿Qué letra sigue en la secuencia A, C, E, G, ...?": "I",
            "Si un tren sale a las 3 p.m. y tarda 2 horas en llegar a su destino, ¿a qué hora llegará?": "5 pm"
        }

    def mostrar_pregunta(self, fila, columna):
        # Dependiendo de la fila, mostramos un tipo de acertijo
        if fila == 0:
            preguntas = list(self.acertijos_numericos.keys())
        elif fila == 1:
            preguntas = list(self.acertijos_cultura.keys())
        elif fila == 2:
            preguntas = list(self.acertijos_secuencia.keys())
        else:
            return None

        numero_acertijo = columna  # Cada columna tendrá un acertijo diferente dentro de la fila
        if 0 <= numero_acertijo < len(preguntas):
            return preguntas[numero_acertijo]
        else:
            return None

    def validar_respuesta(self, fila, columna, respuesta_usuario):
        # Seleccionamos la categoría de acertijo basado en la fila
        if fila == 0:
            respuestas = self.acertijos_numericos
        elif fila == 1:
            respuestas = self.acertijos_cultura
        elif fila == 2:
            respuestas = self.acertijos_secuencia
        else:
            return False

        pregunta = self.mostrar_pregunta(fila, columna)
        respuesta_correcta = respuestas.get(pregunta)
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            print("¡Respuesta correcta! Has ganado 5 puntos de vida, 2 de ataque y 2 de defensa.")

            IniciarJuego.IniciarJuego.jugador.vida += 2
            IniciarJuego.IniciarJuego.jugador.fuerza += 2
            IniciarJuego.IniciarJuego.jugador.defensa += 2

            print(" Vida: " + str(IniciarJuego.IniciarJuego.jugador.vida) +
                  " Fuerza: " + str(IniciarJuego.IniciarJuego.jugador.fuerza) +
                  " Defensa: " + str(IniciarJuego.IniciarJuego.jugador.defensa))
            return True
        else:
            print("Respuesta incorrecta. Inténtalo de nuevo.")
            return False

    def iniciar_pregunta(self):
        fila, columna = self.Mapa.posicion_actual  # Obtiene la posición actual en el mapa
        pregunta = self.mostrar_pregunta(fila, columna)

        if pregunta:
            print(f"Acertijo en habitación ({fila}, {columna}): {pregunta}")
            respuesta_usuario = input("Tu respuesta: ")
            if self.validar_respuesta(fila, columna, respuesta_usuario):
                print("Acertijo completado.\n")
                if self.Mapa.resolver_habitacion():  # Verificar si todas las habitaciones están resueltas
                    return True  # Retornar True si todas están resueltas
            else:
                print("Intenta de nuevo.\n")
        else:
            print("No hay acertijos para esta posición.")
