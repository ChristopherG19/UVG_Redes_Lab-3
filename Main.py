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

# Imports 
from utils.view import *

# Programa principal
def main():

    # Bienvenida al usuario

    # Inicio del programa
    running = True
    while(running):
        
        op_MM = mainMenu()

        if (op_MM == 1):
            # Dijkstra
            print("Dijkstra")

        elif (op_MM == 2):
            # Flooding
            print("Flooding")

        elif (op_MM == 3):
            # Distance Vector Routing
            print("Distance Vector Routing")

        elif (op_MM == 4):
            # Salir del programa
            print("\nGracias por usar el programa.\nAdiós\n")
            running = False



if __name__ == "__main__":
    main()