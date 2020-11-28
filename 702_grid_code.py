import random
       
class Node:
    def __init__(self, position):
        self.position = position
        self.connections = []
        self.node_weight = random.randint(0,9)
    
    
    
    def get_connections(self):
        #check that width and height are the right way round
        
        if self.position[1]+1 <= self.width:
            self.connections.append((self.position[0], self.position[1]+1))
        
        if self.position[1]-1 >= 0:
            self.connections.append((self.position[0], self.position[1]-1))
        
        if self.position[0]+1 <=self.height:
            self.connections.append((self.position[0]+1, self.position[1]))
        
        if self.position[0]-1 >= 0:
            self.connections.append((self.position[0]-1, self.position[1]))
    


class Grid:
    def __init__(self, height, width):
        
        self.height = height
        self.width = width
        
        self.nodes = []
        
    # start the 'get distance process here?
    
    def get_nodes(self):
        for row in self.height:
            for node in self.width:
                #instantiate a node
                self.nodes.append(Node((row,node))) #will input to Node() be too deep?
            
    
    def get_node_connections(self):
        for node in self.nodes:
            node.get_connections()
            
#another class for djikstra?
                