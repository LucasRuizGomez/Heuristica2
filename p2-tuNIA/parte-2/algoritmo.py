import math
from abierta import Abierta
from cerrada import Cerrada

class AlgoritmoAEstrella:
    def __init__(self, mapa):
        self.mapa = mapa

    def heuristica(self, nodo_actual, nodo_destino):
        #return 0  # <--- AÑADE ESTO, GUARDA Y EJECUTA
        """
        Calcula la distancia en línea recta (Euclídea) entre dos puntos.
        """
        pos_a = self.mapa.get_posicion(nodo_actual)
        pos_b = self.mapa.get_posicion(nodo_destino)
        
        # Si no hay coordenadas, devolvemos 0 (se comportaría como Dijkstra)
        if pos_a == (0,0) or pos_b == (0,0):
            return 0
            
        # Fórmula de distancia: raíz((x1-x2)^2 + (y1-y2)^2)
        dx = pos_a[0] - pos_b[0]
        dy = pos_a[1] - pos_b[1]
        return math.sqrt(dx**2 + dy**2)

    def resolver(self, origen, destino):
        # 1. Preparamos las listas
        abierta = Abierta()
        cerrada = Cerrada()
        
        # Estructura para recordar el camino: {hijo: padre}
        padres = {} 
        
        # 2. Metemos el nodo inicial en la lista Abierta
        # f = 0 + h, g = 0
        h_inicial = self.heuristica(origen, destino)
        abierta.put(origen, h_inicial, 0, None) 
        
        nodos_expandidos = 0
        
        # 3. Bucle principal: mientras queden opciones...
        while not abierta.is_empty():
            # Sacamos el nodo con mejor pinta (menor f)
            f, actual, g, padre = abierta.pop()
            
            # Si ya visitamos este nodo con un camino mejor o igual, pasamos
            if cerrada.contains(actual):
                if g >= cerrada.get_g(actual):
                    continue
                
            # Lo marcamos como visitado (Cerrada)
            cerrada.add(actual, g)
            padres[actual] = padre
            nodos_expandidos += 1
            
            # ¡ÉXITO! ¿Hemos llegado al destino?
            if actual == destino:
                camino = self.reconstruir_camino(padres, destino)
                return camino, g, nodos_expandidos
            
            # Si no, miramos a sus vecinos
            vecinos = self.mapa.get_vecinos(actual)
            for vecino in vecinos:
                coste_tramo = self.mapa.get_coste(actual, vecino)
                nuevo_g = g + coste_tramo
                
                # Si ya está cerrado con mejor coste, lo ignoramos
                if cerrada.contains(vecino) and cerrada.get_g(vecino) <= nuevo_g:
                    continue
                
                # Calculamos la prioridad f = g + h
                h = self.heuristica(vecino, destino)
                nuevo_f = nuevo_g + h
                
                # Lo añadimos a pendientes
                abierta.put(vecino, nuevo_f, nuevo_g, actual)
                
        # Si salimos del while, es que no hay camino posible
        return None, 0, nodos_expandidos

    def reconstruir_camino(self, padres, destino):
        """Reconstruye la ruta yendo hacia atrás desde el destino"""
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = padres.get(actual) # Buscamos a su padre
        return camino[::-1] # Le damos la vuelta a la lista