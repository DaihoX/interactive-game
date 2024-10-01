class SistemaPreguntas:
    def __init__(self):
        self.preguntas = []  # Inicializamos la pila vacía

    def agregar_pregunta(self, pregunta):
        """Agrega una nueva pregunta a la pila."""
        self.preguntas.append(pregunta)
        print(f"Pregunta agregada: '{pregunta}'")

    def responder_pregunta(self):
        """Responde y elimina la última pregunta agregada."""
        if not self.esta_vacia():
            pregunta = self.preguntas.pop()  # Elimina y devuelve la última pregunta
            print(f"Respondiendo a la pregunta: '{pregunta}'")
        else:
            print("No hay preguntas por responder")

    def mostrar_ultima_pregunta(self):
        """Muestra la última pregunta agregada sin eliminarla."""
        if not self.esta_vacia():
            print(f"La última pregunta es: '{self.preguntas[-1]}'")
        else:
            print("No hay preguntas disponibles")

    def esta_vacia(self):
        """Verifica si la pila de preguntas está vacía."""
        return len(self.preguntas) == 0


# Ejemplo de uso
sistema = SistemaPreguntas()

# Agregar preguntas
sistema.agregar_pregunta("¿Qué es una pila?")
sistema.agregar_pregunta("¿Cómo funciona el sistema de preguntas?")
sistema.agregar_pregunta("¿Qué es Python?")

# Mostrar la última pregunta
sistema.mostrar_ultima_pregunta()

# Responder preguntas
sistema.responder_pregunta()  # Responde: ¿Qué es Python?
sistema.responder_pregunta()  # Responde: ¿Cómo funciona el sistema de preguntas?

# Mostrar la última pregunta
sistema.mostrar_ultima_pregunta()

# Responder la última pregunta
sistema.responder_pregunta()  # Responde: ¿Qué es una pila?

# Intentar responder cuando no hay más preguntas
sistema.responder_pregunta()
