"""
Universidad del Valle de Guatemala
Facultad de Ingeniería
Departamento de Ciencias de la Computación
CC3067 - Redes

Laboratorio 3 - Primera Parte 
Algoritmos de Enrutamiento

Integrantes:
- Christopher García (20541)
- José Rodrigo Barrera (20807)
- Ma. Isabel Solano (20504)
"""

import json
from extras import Node

class Flooding():
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
        
    def flood(self, source_node, message):
        message_data = json.loads(message)
        message_type = message_data["type"]
        headers = message_data["headers"]
        
        for neighbor in source_node.get_neighbors():
            if neighbor != headers['from']:
                print(f"Reenvia este paquete a: {neighbor.name}")
                print(message)
                print()
                self.flood(neighbor, message)
    
            else:
                if(not source_node.get_visited()):
                    source_node.set_visited(True)
                    if(message_type == "info"):
                        print("Mensaje de información recibida:", headers)
                        print()
                    elif(message_type == "message"):
                        if(source_node.name == headers['to']):
                            print(f"({source_node.name}) Mensaje entrante de: {headers['from']}")
                            print(message_data["payload"], "\n")

    def initiate_flood(self, source_node, message_data, destiny):
        for node in self.nodes:
            node.visited = False  # Reiniciar el estado visitado de todos los nodos
        message = self.create_message(source_node, message_data, destiny)
        self.flood(source_node, message)
            
    def create_message(self, source_node, message_data, destiny):
        headers = {
            "from": source_node.name,
            "to": destiny.name,
            "hop_count": len(self.nodes)
        }
        
        payload = message_data

        message = {
            "type": "message",
            "headers": headers,
            "payload": payload
        }
        
        return json.dumps(message, indent=4)
            
    def start(self):
        print()
        name = input("Nombre del nodo actual: ")
        actual_node = Node(name)
        self.add_node(actual_node)
        ver = False
        while(not ver):
            res = input("Desea ingresar vecinos? (y/n): ")
            if(res.lower() == "y"):
                name_node = input("Nombre del nodo vecino: ")
                new_node = Node(name_node)
                actual_node.add_neighbor(new_node)
                self.add_node(new_node)
                
            elif(res.lower() == "n"):
                if(len(actual_node.neighbors) > 0):
                    print("Entendido, continuando con el programa...")
                    ver = True
                else:
                    print("Lo siento pero no manejamos nodos sin vecinos")
                    print("Esto dificulta la comunicación")
                
            else:
                print("Ingresa una opción correcta!!!")
                
        print("\nDatos ingresados\n")
        for el in self.nodes:
            print(el)
        
        ver2 = False
        while(not ver2):
            print("\n1) Enviar mensaje")
            print("2) Recibir mensaje")
            print("3) Salir")
            op = int(input("Ingresa opcion: "))
            
            match op:
                case 1:
                    sour = actual_node
                    dest = input("Nombre de nodo destino: ")
                    msg = input("Ingresa el mensaje que deseas enviar: ")
                    
                    print()
                    
                    node_dest = None
                    for node in self.nodes:
                        if node.name == dest:
                            node_dest = node
                    
                    if(node_dest):
                        self.initiate_flood(sour, msg, node_dest)
                    else:
                        print("Nodo no alcanzable")
                    
                case 2:
                    0
                case 3:
                    print("Entendido, saliendo...")
                    ver2 = True
        
        