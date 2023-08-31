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

    def flood(self, message):
        message_data = json.loads(message)
        message_type = message_data["type"]
        headers = message_data["headers"]
        
        if(not self.visited):
            self.visited = True
            if(message_type == "info"):
                print("Mensaje de información recibida:", headers)
                print()
            elif(message_type == "message"):
                if(self.name == headers['to']):
                    print(f"({self.name}) Mensaje entrante de: {headers['from']}")
                    print(message_data["payload"], "\n")
                else:
                    print(f"Reenvia este paquete a: {headers['to']}")
                    print(message)
                    print()
                    # for neighbor in self.neighbors:
                    #     if neighbor != headers['from']:
                    #         neighbor.flood(message)
        
    def __repr__(self):
        return f"Nodo: {self.name}{(' | Vecinos: '+str(self.neighbors)) if len(self.neighbors)>0 else ''}"
        
    def __str__(self):
        return f"Nodo: {self.name}{(' | Vecinos: '+str(self.neighbors)) if len(self.neighbors)>0 else ''}"