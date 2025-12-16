import heapq

class Abierta:
    def __init__(self):
        # Usamos una cola de prioridad (heap) para sacar siempre el mejor nodo rápido
        self.cola = [] 
        
    def put(self, nodo, f, g, padre):
        """
        Añade un nodo a la lista de pendientes.
        nodo: ID de la ciudad
        f: coste total estimado (distancia recorrida + distancia a meta)
        g: distancia real ya recorrida
        padre: de qué ciudad venimos (para luego reconstruir el camino)
        """
        # Guardamos una tupla. Python ordena automáticamente por el primer número (f)
        heapq.heappush(self.cola, (f, nodo, g, padre))

    def pop(self):
        """Saca y devuelve el mejor nodo (el que tenga menor f)"""
        if self.is_empty():
            return None
        return heapq.heappop(self.cola)

    def is_empty(self):
        return len(self.cola) == 0