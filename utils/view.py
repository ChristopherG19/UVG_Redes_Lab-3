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