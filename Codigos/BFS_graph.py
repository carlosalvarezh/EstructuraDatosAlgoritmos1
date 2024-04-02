from collections import defaultdict

# Clase para representar un grafo
class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    # Función para agregar una arista al grafo
    def agregar_arista(self, u, v):
        self.grafo[u].append(v)

    # Función para realizar el recorrido BFS
    def bfs(self, inicio):
        # Verificar que el nodo de inicio es válido
        if inicio > max(self.grafo):
            print("El nodo de inicio es mayor que el nodo máximo en el grafo.")
            return

        # Lista para almacenar los nodos visitados
        visitados = [False] * (len(self.grafo) + 1)

        # Cola para el recorrido BFS
        cola = []

        # Marcar el nodo inicial como visitado y agregarlo a la cola
        visitados[inicio] = True
        cola.append(inicio)

        while cola:
            # Sacar un nodo de la cola y mostrarlo
            nodo = cola.pop(0)
            print(nodo, end=" ")

            # Obtener todos los nodos adyacentes al nodo actual
            # Si no han sido visitados, marcarlos como visitados y agregarlos a la cola
            for adyacente in self.grafo[nodo]:
                if not visitados[adyacente]:
                    visitados[adyacente] = True
                    cola.append(adyacente)

# Crear un objeto de la clase Grafo
grafo = Grafo()

# Agregar las aristas al grafo
aristas = [(0, 1), (0, 2), (1, 3), (1, 2), (2, 4), (3, 4)]
for u, v in aristas:
    grafo.agregar_arista(u, v)

# Realizar el recorrido BFS desde el nodo 0
print("Recorrido BFS:")
if len(grafo.grafo) > 0:
    grafo.bfs(0)
else:
    print("El grafo está vacío.")