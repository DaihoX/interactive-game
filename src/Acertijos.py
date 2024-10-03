import Mapa
from Habitacion import Habitacion
from Mapa import Mapa

class Acertijos:
    def __init__(self):
        
        self.Mapa = Mapa()
        # Diccionario con preguntas como claves y respuestas correctas como valores
        self.acertijos = {
            "¿Cuánto es 5 + 5?": "10",
            
        }

    def mostrar_pregunta(self, numero_acertijo):
   
        # Convertir las preguntas en una lista y obtener la pregunta por su índice
        preguntas = list(self.acertijos.keys())
        if 0 <= numero_acertijo < len(preguntas):
            return preguntas[numero_acertijo]
        else:
            return None

    def validar_respuesta(self, pregunta, respuesta_usuario):
        
        # Obtener la respuesta correcta del diccionario
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
                    numero_acertijo += 1  # Pasar al siguiente acertijo
                else:
                    print("Intenta de nuevo.\n")
            else:
                print("¡Has completado todos los acertijos!")
                self.Mapa.resolver_habitacion()
                break

# Ejemplo de uso
if __name__ == "__main__":
    juego_acertijos = Acertijos()  # Crear una instancia de la clase
    juego_acertijos.iniciar_juego()  # Iniciar el juego llamando a la clase
