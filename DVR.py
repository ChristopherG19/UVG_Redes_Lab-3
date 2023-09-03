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
import json

class DistanceVectorRouting():
    def __init__(self):
        self.RT = RoutingTable()
        self.Neighbors = []
        pass

    def start(self):
        print("")
        self.actual_node = input("Nombre del nodo actual: ")

        self.RT.addNeighbor(self.actual_node, 0, self.actual_node)

        # ingresar vecinos
        self.DVR_input_initial_neighbors()

        print("Nodos:")
        print(self.RT)

        # iniciar menu interno
        DVR_ = True
        while(DVR_):

            opp = DVR_menu()

            if opp == 1:
                # Actualizar rutas
                0

            elif opp == 2:
                # generar data
                self.writeJSON("info")

            elif opp == 3:
                # diferenciar tipo de mensaje recibido
                file_path = 'input.JSON'
                with open(file_path, 'r') as file:
                    try:
                        
                        input_ = input("Presione enter cuando haya actualizado input.txt ")
                        jsonReceived = json.load(file)
                        mtype = jsonReceived["type"]

                        if mtype == "info":
                            0
                        
                        elif mtype == "echo":
                            0

                        elif mtype == "message":
                            
                            if jsonReceived["headers"]["to"] != self.actual_node:
                                # Re-send
                                0

                            else:
                                # Read
                                from_ = jsonReceived["headers"]["from"]
                                mess= jsonReceived["payload"]
                                print("\n================================")
                                print(f"Mensaje recibido de {from_}")
                                print(f"{mess}")
                                print("================================")


                        else:
                            print("[[Error, no existe el tipo]]")

                    except FileNotFoundError:
                        print(f"File not found: {file_path}")
                    except json.JSONDecodeError as e:
                        print("Error parsing JSON:", e)

            elif opp == 4:
                print(self.RT)

            elif opp == 5:
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

                if v not in self.Neighbors:
                    self.Neighbors.append(v)

                print("\nDesea continuar agregando nodos?")
                op = input("(y/n): ")

                if op.lower() == "n":
                    addN = False
                

            except ValueError:
                print("\n[[Error, input inválido]]\n")

    def receiveRT(self, rt: RoutingTable):
        0

    def writeJSON(self, type_):
        if type_ == "info":

            print("Por favor copie y envíe los siguientes mensajes:")

            payload = self.RT.TABLE

            for n in self.Neighbors:
                headers = {
                    "from": self.actual_node,
                    "to": n
                }

                message = {
                    "type": "info",
                    "headers": headers,
                    "payload": payload
                }

                print("")
                jsonRes = json.dumps(message, indent=4)
                print(jsonRes)

        if type_ == "message":
            0
