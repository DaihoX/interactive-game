class Habitacion:
    def __init__(self):
        self.resuelto = False

    def resolver(self):
        if self.resuelto:
            print("¡Habitación ya resuelta! Ve a otra.")
        else:
            self.resuelto = True