import Mapa
from Habitacion import Habitacion
from Mapa import Mapa


class Acertijos:
    def __init__(self, mapa):
        self.Mapa = mapa
        self.acertijos = {
            "¿Cuánto es 5 + 5?": "10",
            "Cual es la capital de Francia": "Paris",
        }

    def mostrar_pregunta(self, numero_acertijo):
        preguntas = list(self.acertijos.keys())
        if 0 <= numero_acertijo < len(preguntas):
            return preguntas[numero_acertijo]
        else:
            return None

    def validar_respuesta(self, pregunta, respuesta_usuario):
        respuesta_correcta = self.acertijos.get(pregunta)
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            print("¡Respuesta correcta!")
            return True
        else:
            print("Respuesta incorrecta. Inténtalo de nuevo.")
            return False

    def iniciar_pregunta(self):
        numero_acertijo = 0
        while True:
            pregunta = self.mostrar_pregunta(numero_acertijo)
            if pregunta:
                print(f"Acertijo {numero_acertijo + 1}: {pregunta}")
                respuesta_usuario = input("Tu respuesta: ")
                if self.validar_respuesta(pregunta, respuesta_usuario):
                    print("Acertijo completado.\n")
                    self.Mapa.resolver_habitacion()  # Llamar al método para resolver la habitación  # Llamar al método para resolver la habitación
                    numero_acertijo += 1
                else:
                    print("Intenta de nuevo.\n")
            else:
                print("¡Has completado todos los acertijos!")
                break
