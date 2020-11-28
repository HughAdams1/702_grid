import random

       
class Node:
    def __init__(self, position):
        self.position = position
        self.connections = []
        self.node_weight = random.randint(0,9)
        self.distance = 10,000
    
    
    
    def get_connections(self):
        #check that width and height are the right way round
        
        if self.position[1]+1 <= self.width:
            self.connections.append((self.position[0], self.position[1]+1))
        #error, node has no 'width'
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
        for row in range(self.height):
            row_of_nodes = []
            for node in range(self.width):
                #instantiate a node
                row_of_nodes.append(Node((row,node))) #will input to Node() be too deep?
            self.nodes.append(row_of_nodes)
            
    
    def get_node_connections(self):
        for row in range(self.height):
            for node in range(self.width):
                self.nodes[row][node].get_connections()
            
class Djikstra:
    def __init__(self, location):
        #make the line below fetch it from another class
        self.location = self.nodes[height][0] 
    
    #def options(self):



###################### Testing ##########################
my_grid = Grid(3,4)
my_grid.get_nodes()
my_grid.get_node_connections() 
    
    
my_grid.nodes
    
    
    
    
    
    
    
    
    
    
    
    
                