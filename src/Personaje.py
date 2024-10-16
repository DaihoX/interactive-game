class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Metedo para retornar si el personaje esta vivo
    def esta_vivo(self):
        return self.vida > 0

    # Metodo para matar al personaje
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Metodo para calcular el daño que se le hara al enemigo
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Metodo para atacar al enemigo
    def atacar(self, enemigo):

        # Calcular el daño que se le hara al enemigo
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)

        # Mostrar la vida del enemigo
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)

        # Si el enemigo muere, se llama
        else:
            enemigo.morir()
