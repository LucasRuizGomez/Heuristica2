#NO podemos usar heapq --> Profesores en el foro



class Abierta:
    def __init__(self):
        self.cola = []  # lista de tuplas (f, nodo, g, padre)

    def put(self, nodo, f, g, padre):
        # añadimos al final
        self.cola.append((f, nodo, g, padre))

    def pop(self):
        if self.is_empty():
            return None

        # buscamos el índice con menor f
        indice_mejor = 0
        mejor_f = self.cola[0][0]

        for i in range(1, len(self.cola)):
            f = self.cola[i][0]
            if f < mejor_f:
                mejor_f = f
                indice_mejor = i

        # sacamos y devolvemos ese elemento
        return self.cola.pop(indice_mejor)

    def is_empty(self):
        return len(self.cola) == 0