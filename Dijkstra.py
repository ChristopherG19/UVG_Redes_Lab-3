import json

class Graph:
    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        self.nodes.add(node)

class Node:
    def __init__(self, name):
        self.name = name
        self.shortest_path = []
        self.distance = float('inf')
        self.adjacent_nodes = {}

    def add_destination(self, destination, distance):
        self.adjacent_nodes[destination] = distance



class Dijkstra():
    def __init__(self):
        pass
    
    def get_lowest_distance_node(self, unsettled_nodes):
        lowest_distance_node = None
        lowest_distance = float('inf')
        
        for node in unsettled_nodes:
            node_distance = node.distance
            if node_distance < lowest_distance:
                lowest_distance = node_distance
                lowest_distance_node = node
        
        return lowest_distance_node
    
    def calculate_minimum_distance(self, evaluation_node, edge_weight, source_node):
        source_distance = source_node.distance
        if source_distance + edge_weight < evaluation_node.distance:
            evaluation_node.distance = source_distance + edge_weight
            shortest_path = source_node.shortest_path.copy()
            shortest_path.append(source_node)
            evaluation_node.shortest_path = shortest_path
    
    def calculate_shortest_path_from_source(self, graph, source):
        source.distance = 0

        settled_nodes = set()
        unsettled_nodes = set()

        unsettled_nodes.add(source)

        while unsettled_nodes:
            current_node = self.get_lowest_distance_node(unsettled_nodes)
            unsettled_nodes.remove(current_node)
            
            for adjacent_node, edge_weight in current_node.adjacent_nodes.items():
                if adjacent_node not in settled_nodes:
                    self.calculate_minimum_distance(adjacent_node, edge_weight, current_node)
                    unsettled_nodes.add(adjacent_node)
            
            settled_nodes.add(current_node)
        
        return graph
    
    def create_message(self, source_node, destination_node, message):
        shortest_path = destination_node.shortest_path
        hop_count = len(shortest_path) - 1
        headers = {
            "from": source_node.name,
            "to": destination_node.name,
            "hop_count": hop_count
        }
        payload = message

        message_data = {
            "type": "info",
            "headers": headers,
            "payload": payload
        }
        
        return json.dumps(message_data, indent=4)

    def create_info_messages(self, source_node, message):
        info_messages = []

        for adjacent_node, edge_weight in source_node.adjacent_nodes.items():
            hop_count = len(adjacent_node.shortest_path) - 1
            headers = {
                "from": source_node.name,
                "to": adjacent_node.name,
                "hop_count": hop_count
            }
            payload = message

            message_data = {
                "type": "info",
                "headers": headers,
                "payload": payload
            }

            info_messages.append(json.dumps(message_data, indent=4))

        return info_messages
    

    def process_message(self, message_json, receiving_node):
        message_data = json.loads(message_json)
        message_type = message_data["type"]
        headers = message_data["headers"]

        if message_type == "info":
            # Process information message, decide which neighbors to forward it to
            # based on the shortest path
            # Example: Decide based on headers["to"]
            print("Received info message:", headers)
        elif message_type == "message":
            # Process user message, check if it has reached the destination
            if headers["to"] == receiving_node.name:
                print("Received user message:", message_data["payload"])
            else:
                print("Forwarding user message to:", headers["to"])
                # Forward the message to the next node in the shortest path
                # Example: headers["to"] corresponds to the next node
    
    def main(self):
        graph = Graph()

        nodeA = Node("A")
        nodeB = Node("B")
        nodeC = Node("C")
        nodeD = Node("D")
 

        nodeA.add_destination(nodeB, 10)
        nodeA.add_destination(nodeC, 15)

        nodeB.add_destination(nodeD, 12)
        nodeC.add_destination(nodeD, 10)


        graph.add_node(nodeA)
        graph.add_node(nodeB)
        graph.add_node(nodeC)
        graph.add_node(nodeD)

        graph = self.calculate_shortest_path_from_source(graph, nodeA)

        while True:
            print("1. Send Message")
            print("2. Listen for Messages")
            print("3. Exit")
            
            choice = input("Select an option: ")
            
            if choice == "1":
                source_node = nodeA
                destination_node = nodeD
                message = input("Enter your message: ")
                info_messages = self.create_info_messages(source_node, message)
                for info_message in info_messages:
                    print("Sending info message:")
                    print(info_message)
            elif choice == "2":
                print("Enter the message JSON (press Enter twice to finish):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    lines.append(line)
                message_json = "\n".join(lines)
                receiving_node = nodeD  
                self.process_message(message_json, receiving_node)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    