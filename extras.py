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


class Node:
    def __init__(self, name):
        self.name = name.upper()
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_neighbors(self):
        return self.neighbors
    
    def get_visited(self):
        return self.visited
    
    def set_visited(self, vis):
        self.visited = vis
        
    def __repr__(self):
        return f"Nodo: {self.name}{(' | Vecinos: '+str(self.neighbors)) if len(self.neighbors)>0 else ''}"
        
    def __str__(self):
        return f"Nodo: {self.name}{(' | Vecinos: '+str(self.neighbors)) if len(self.neighbors)>0 else ''}"