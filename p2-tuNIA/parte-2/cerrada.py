class Cerrada:
    def __init__(self):
        # Diccionario para guardar {nodo: coste_g_para_llegar_aqui}
        self.visitados = {}

    def add(self, nodo, g):
        """Marca un nodo como visitado con su coste g"""
        self.visitados[nodo] = g

    def contains(self, nodo):
        """¿Ya hemos visitado este nodo?"""
        return nodo in self.visitados

    def get_g(self, nodo):
        """Devuelve el coste g con el que visitamos el nodo (si existe)"""
        return self.visitados.get(nodo, float('inf'))