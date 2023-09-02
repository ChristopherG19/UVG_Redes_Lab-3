from prettytable import PrettyTable

class RoutingTable():
    def __init__(self) -> None:
        self.TABLE = []

    def addNeighbor(self, name, weight, hop):
        temp = [name, weight, hop]
        self.TABLE.append(temp)

    def updateNeighbor(self, name, weight, hop):
        0

    def contains(self, name):
        for i in self.TABLE:
            if i[0] == name:
                return True
        return False
    
    def get_info(self, name):
        for i in self.TABLE:
            if i[0] == name:
                return (i[1], i[2])
        return None 
    
    def update_info(self, name, weight, hop):
        for i in range(len(self.TABLE)):
            if i == 0:
                # Es el primer nodo y sí mismo
                print("No se puede editar el propio")
                return
            
            if self.TABLE[i][0] == name:
                self.TABLE[i][1] = weight
                self.TABLE[i][2] = hop
    
    def __repr__(self) -> str:
        t = PrettyTable()
        t.field_names = ["Node", "Weight", "Hop"]
        for n in self.TABLE:
            t.add_row(n)

        return t.get_string()