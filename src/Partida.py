import pickle

class Partida:
    def __init__(self, archivo="partida_guardada.pkl"):
        self.archivo = archivo

    def guardar(self, mapa):
        try:
            with open(self.archivo, 'wb') as f:
                pickle.dump(mapa, f)
            print(f"Partida guardada en {self.archivo}")
        except Exception as e:
            print(f"Error al guardar la partida: {e}")

    def cargar(self):
        try:
            with open(self.archivo, 'rb') as f:
                mapa = pickle.load(f)
            print(f"Partida cargada desde {self.archivo}")
            return mapa
        except FileNotFoundError:
            print(f"No se encontró el archivo {self.archivo}")
        except Exception as e:
            print(f"Error al cargar la partida: {e}")
        return None
    
    