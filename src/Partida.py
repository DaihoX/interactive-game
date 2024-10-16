import pickle


class Partida:
    def __init__(self, archivo="partida_guardada.pkl"):
        self.archivo = archivo

    def guardar(self, mapa, acertijos):
        try:
            with open(self.archivo, 'wb') as f:
                # Guardamos un diccionario que contiene ambos objetos: el mapa y los acertijos
                pickle.dump({'mapa': mapa, 'acertijos': acertijos}, f)
            print(f"Partida y acertijos guardados en {self.archivo}")
        except Exception as e:
            print(f"Error al guardar la partida y los acertijos: {e}")

    def cargar(self):
        try:
            with open(self.archivo, 'rb') as f:
                data = pickle.load(f)
                mapa = data['mapa']
                acertijos = data['acertijos']
            print(f"Partida y acertijos cargados desde {self.archivo}")
            return mapa, acertijos
        except FileNotFoundError:
            print(f"No se encontró el archivo {self.archivo}")
        except Exception as e:
            print(f"Error al cargar la partida y los acertijos: {e}")
        return None, None