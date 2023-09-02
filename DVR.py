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

from utils.view import *
from utils.RT import *

class DistanceVectorRouting():
    def __init__(self):
        self.RT = RoutingTable()
        pass

    def start(self):
        print("")
        actual_node = input("Nombre del nodo actual: ")

        self.RT.addNeighbor(actual_node, 0, actual_node)

        # ingresar vecinos
        self.DVR_input_initial_neighbors()

        print("Nodos:")
        print(self.RT)

        # iniciar menu interno
        DVR_ = True
        while(DVR_):

            opp = DVR_menu()

            if opp == 1:
                0

            elif opp == 2:
                0

            elif opp == 3:
                # Salir 
                DVR_ = False

    def DVR_input_initial_neighbors(self):
        addN = True

        print("A continuación ingrese la información de los vecinos")

        while (addN):
            try:
                v = input("\nNombre: ")
                w = int(input("Peso: "))

                if self.RT.contains(v):
                    # Update
                    print("El nodo ya existía, se reescribirá con la nueva información")
                    self.RT.update_info(v, w, v)

                else:
                    # Add to table
                    self.RT.addNeighbor(v, w, v)

                print("\nDesea continuar agregando nodos?")
                op = input("(y/n): ")

                if op.lower() == "n":
                    addN = False
                

            except ValueError:
                print("\n[[Error, input inválido]]\n")
