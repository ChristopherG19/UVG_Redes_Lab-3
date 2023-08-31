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

class Node:
    def __init__(self, name):
        self.name = name.upper()
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def flood(self, message):
        if not self.visited:
            self.visited = True
            if(self.name == message['destiny']):
                print(f"Nodo {self.name} recibió: {message['data']}")
            else:
                print(f"Nodo {self.name} reenvió paquete a: {message['destiny']}")
                for neighbor in self.neighbors:
                    if neighbor != message['source']:
                        neighbor.flood(message)
        
    def __repr__(self):
        return f"Nodo: {self.name}{(' | Vecinos: '+str(self.neighbors)) if len(self.neighbors)>0 else ''}"
        
    def __str__(self):
        return f"Nodo: {self.name}{(' | Vecinos: '+str(self.neighbors)) if len(self.neighbors)>0 else ''}"