class Flooding():
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def initiate_flood(self, source_node, message_data):
        for node in self.nodes:
            node.visited = False  # Reiniciar el estado visitado de todos los nodos
        source_node.visited = True  # Marcar el nodo emisor como visitado
        message = {'source': source_node, 'data': message_data}
        for neighbor in source_node.neighbors:
            neighbor.flood(message)
    
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def flood(self, message):
        if not self.visited:
            print(f"Node {self.name} received message: {message['data']}")
            self.visited = True
            for neighbor in self.neighbors:
                if neighbor != message['source']:
                    neighbor.flood(message)

# Ejemplo de prueba
                
# Crear instancias de nodos
node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')

# Establecer conexiones entre nodos
node_A.add_neighbor(node_B)
node_A.add_neighbor(node_C)
node_B.add_neighbor(node_A)
node_B.add_neighbor(node_D)
node_C.add_neighbor(node_A)
node_C.add_neighbor(node_E)
node_D.add_neighbor(node_B)
node_D.add_neighbor(node_F)
node_E.add_neighbor(node_C)
node_E.add_neighbor(node_F)
node_F.add_neighbor(node_D)
node_F.add_neighbor(node_E)

# Crear instancia de la clase Flooding
flooding = Flooding()

# Agregar nodos a la instancia de Flooding
flooding.add_node(node_A)
flooding.add_node(node_B)
flooding.add_node(node_C)
flooding.add_node(node_D)
flooding.add_node(node_E)
flooding.add_node(node_F)

# Iniciar la inundación desde un nodo
flooding.initiate_flood(node_A, "Hello, everyone!")