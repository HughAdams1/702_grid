import random
#from abc import ABC, abstractmethod
import numpy as np

class Node:
    def __init__(self, node_position):
        #self.grid_height = grid_height
        #self.grid_width = grid_width
        self.node_position = node_position
        self.connections = []
        #set initial distance of node higher than any that could be generated on grid
        self.distance = 10000.
        self.weight = random.randint(0,9)
        self.previous_node = 0
    

#class Algorithm(ABC):
#make djikstra subclass of algorithm
 
#djikstra works by:
#calculate distance of neighbours
#move to node with smallest distance
#calculate distance of neighbours on new node



            
            
class Dijkstra():
    def __init__(self, height, width):
        #super().__init__(height, width)
        #self.current_node = self.nodes[self.width - 1][0]

        self.visited_nodes = []
        self.seen_but_not_visited_nodes = []

        self.height = height
        self.width = width        
        self.nodes = []
            
    def get_grid_nodes(self):
        for row in range(self.height):
            row_of_nodes = []
            for column in range(self.width):
                node_position = (row,column)
                row_of_nodes.append(Node(node_position))
            self.nodes.append(row_of_nodes)
        
    def get_to_starting_position(self, starting_position =(0,0)):
        self.current_node = self.nodes[starting_position[0]][starting_position[1]]
        self.current_node.distance = 0
        
        
    def get_node_connections(self):
        for row in range(self.height):
            for column in range(self.width):
                node = self.nodes[row][column]

                if column < self.width-1:
                    node.connections.append(self.nodes[row][column+1])
                #error, node has no 'width'
                if column > 0:
                    node.connections.append(self.nodes[row][column-1])
                
                if row < self.height-1:
                    node.connections.append(self.nodes[row+1][column])
                #error, node has no 'width'
                if row > 0:
                    node.connections.append(self.nodes[row-1][column])
        
    def update_connection_distances(self):
        #get current node connection distances
        for connection in self.current_node.connections:
            #the problem is with node_weight, it is empty
            new_distance = connection.weight + self.current_node.distance
            # will never relabel the node it just came off
            if connection.distance > new_distance:
                connection.distance = new_distance
                #update current node
                connection.previous_node = self.current_node
            #add connections of current node to seen nodes list        
            self.seen_but_not_visited_nodes.append(connection)
            
        #make sure there are no repeated nodes in seen nodes
        temp_list = []
        [temp_list.append(i) for i in self.seen_but_not_visited_nodes if i not in temp_list]
        self.seen_but_not_visited_nodes = temp_list
        #make sure no node is visited twice
        self.seen_but_not_visited_nodes = [
            i for i in self.seen_but_not_visited_nodes if i not in self.visited_nodes
            ]
                    
    def move(self):
        #move to an unvisited node that has the smallest distance
        #all unseen nodes have distance of 10,000, node with smallest distance
        #is a seen node always
        if len(self.seen_but_not_visited_nodes)>0:
            best_move = self.seen_but_not_visited_nodes[0]
            for node in self.seen_but_not_visited_nodes:
                if node.distance < best_move.distance:
                    best_move = node
                    
            self.current_node = best_move
                    
            self.visited_nodes.append(best_move)
                    
            self.seen_but_not_visited_nodes.remove(best_move)
                    #or 
            #self.seen_but_not_visited_nodes = [
             #   i for i in self.seen_but_not_visited_nodes if i not in self.visited_nodes
              #  ]
       
        else:
            print("got distances for all nodes")
        
       
        
    def go(self):
        #self.get_grid_nodes()
        self.get_to_starting_position()
        self.get_node_connections()
        self.update_connection_distances()         
        while len(self.seen_but_not_visited_nodes) > 0:
            print()
            self.move()
            self.update_connection_distances()
    
    def find_path(self):
        final_path_node = self.nodes[self.height-1][self.width-1]
        
        path_node = final_path_node
        print("final distance at node {} is: {}".format(path_node.node_position, path_node.distance))
        path_node = path_node.previous_node
        
        while type(path_node.previous_node) == Node:
            print("The previous node is {} and has distance {}, and weight {}".format(path_node.node_position, path_node.distance, path_node.weight))
            path_node = path_node.previous_node
        
######### dOES IT WORK? #############

my_algorithm = Dijkstra(10,10) 
my_algorithm.get_grid_nodes()      
my_algorithm.go()
my_algorithm.find_path()







#my_algorithm.get_to_starting_position()
#my_algorithm.current_node.node_position

#my_algorithm.get_node_weights()
#my_algorithm.nodes[0][0]

#my_algorithm.get_node_connections()
#my_algorithm.nodes[1][1].distance

#my_algorithm.update_connection_distances()
#my_algorithm.move()
#my_algorithm.current_node.node_position
#my_algorithm.current_node.distance

#my_algorithm.nodes[3][3].distance
#my_algorithm.nodes[3][3].weight
#my_algorithm.nodes[3][3].previous_node.node_position

#type(my_algorithm.nodes[1][3].previous_node) == Node

#path_node = my_algorithm.nodes[3][3]
#while type(path_node.previous_node) == Node:
#    print("The previous node is {} and has distance {}, and weight {}".format(path_node.node_position, path_node.distance, path_node.weight))
#    path_node = path_node.previous_node
#my_algorithm.seen_but_not_visited_nodes
#connection_weights = []
#for connection in my_algorithm.current_node.connections:
#    print(connection)
    
#connection_weights
#my_algorithm.move()
#my_algorithm.current_node.node_position

#y = sum(my_algorithm.nodes[2][3].node_weight, my_algorithm.current_node.distance)
#print(y)





#print(help(Grid))

###################### Testing ##########################
#my_node_1 = Node((3,4))
#my_node_2 = Node((3,5))    
#my_node_1.node_weight
#my_node_2.node_weight

#x = []
#y = [2,3,4,5,5,4]
#y = np.unique(y)
#y    
#[x.append(i) for i in y if i not in x]
#y = x
#print(y)             

#z = [1]
#for i in z:
#    print(i)