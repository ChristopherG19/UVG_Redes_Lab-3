def mainMenu():
    
    while(True):

        print("\n==================================")
        print("Elija el algoritmo a utilizar")
        print("1) Dijkstra")
        print("2) Flooding")
        print("3) Distance Vector Routing")
        print("4) Salir ")
        print("__________________________________")

        op = input("Número de la opción: ")

        if op not in [str(x + 1) for x in range(4)]:
            print("\n[[Error, input inválido]]\n")

        else:
            return int(op)

def DVR_menu():

    while(True):

        print()
        print("1) Enviar mensaje a un nodo")
        print("2) Enviar info a vecinos")
        print("3) Recibir info/mensaje")
        print("4) Mostrar tabla de enrutamiento")
        print("5) Salir")

        op = input("No. de la opción: ")

        if op in ["1", "2", "3", "4", "5"]:
            return int(op)
        
        else:
            print("\n[[Error, input inválido]]\n")