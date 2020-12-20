import random
#from abc import ABC, abstractmethod
import numpy as np
from scipy import stats

class Node:
    def __init__(self, node_position):
        #self.grid_height = grid_height
        #self.grid_width = grid_width
        self.node_position = node_position
        self.connections = []
        #set initial distance of node higher than any that could be generated on grid
        self.distance = 10000.
        self.weight = random.randint(0,9)
        self.previous_node = []
        self.next_node = []
    

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
            new_distance = connection.weight + self.current_node.distance
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
        print("final distance at node {} is: {}, qith weight {}".format(path_node.node_position, path_node.distance, path_node.weight))
        path_node = path_node.previous_node
        
        while type(path_node.previous_node) == Node:
            print("The previous node is {} and has distance {}, and weight {}".format(path_node.node_position, path_node.distance, path_node.weight))
            path_node = path_node.previous_node
        
######### dOES IT WORK? #############

#my_algorithm = Dijkstra(10,10) 
#my_algorithm.get_grid_nodes()      
#my_algorithm.go()
#my_algorithm.find_path()


############################# ACO




class ACO():
    def __init__(self, height, width):
        #super().__init__(height, width)
        #self.current_node = self.nodes[self.width - 1][0]

        self.visited_nodes = []
        self.end = False
        self.height = height
        self.width = width        
        self.nodes = []
        self.end_nodes = []
            
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
                    connection_and_tau = (self.nodes[row][column+1], 1, 0)
                    node.connections.append(connection_and_tau)
                #error, node has no 'width'
                if column > 0:
                    connection_and_tau = (self.nodes[row][column-1], 1, 0)
                    node.connections.append(connection_and_tau)
                
                if row < self.height-1:
                   connection_and_tau = (self.nodes[row+1][column], 1, 0)
                   node.connections.append(connection_and_tau)
                #error, node has no 'width'
                if row > 0:
                    connection_and_tau = (self.nodes[row-1][column], 1, 0)
                    node.connections.append(connection_and_tau)    
        
    
    def one_ant(self):
        self.end = False
        self.visited_nodes = []
        self.get_to_starting_position()
        while self.end == False: 
            self.move()
        self.end_nodes.append(self.current_node.node_position)
        #print("end position is : {}".format(self.current_node.node_position))
        
    def move(self):
        moves = [(x,y,z) for (x,y,z) in self.current_node.connections if x not in self.visited_nodes]
        if len(moves)>0:            
            tau_prob_distribution = [x[1]/(x[0].weight + 0.001) for x in moves]
            tau_prob_distribution = [x[1]/(x[0].weight + 0.001) for x in moves]
            tau_prob_distribution = [x / sum(tau_prob_distribution) for x in tau_prob_distribution]
            new_connection = random.choices(moves, weights = tau_prob_distribution)[0]
            new_connection[0].previous_node = (my_ACO.current_node, new_connection[1], new_connection[2])
            self.current_node.next_node = new_connection
            #move to new node
            self.visited_nodes.append(self.current_node)
            self.current_node = new_connection[0]
            self.current_node.distance = self.current_node.weight + self.current_node.previous_node[0].distance
            self.end = False
        else:
            self.end = True
    def calculate_tau_update(self):
        length_of_path = self.current_node.distance
        
        for row in range(self.height):
            for column in range(self.width):
                node = self.nodes[row][column]
                if len(node.next_node)>0:
                    b = (node.next_node[0], node.next_node[1], node.next_node[2] + 1/length_of_path)
                    node.next_node = b
                if len(node.previous_node)>0:
                    a = (node.previous_node[0], node.previous_node[1], node.previous_node[2] + 1/length_of_path)
                    node.previous_node = a
        
        
        
       # end_point = self.nodes[self.height-1][self.width-1]
       # #starting_point = self.nodes[0][0]
       # while self.current_node.node_position != (0, 0):
       #     if self.current_node == end_point:
       #         a = (self.current_node.previous_node[0], self.current_node.previous_node[1], self.current_node.previous_node[2] + 1/length_of_path)
       #         self.current_node.previous_node = a
       #     else:
       #         a = (self.current_node.previous_node[0], self.current_node.previous_node[1], self.current_node.previous_node[2] + 1/length_of_path)
       #         self.current_node.previous_node = a
       #         b = (self.current_node.next_node[0], self.current_node.next_node[1], self.current_node.next_node[2] + 1/length_of_path)
       #         self.current_node.next_node = b
       #     self.current_node = self.current_node.previous_node[0]
                    
    def go(self, population, trips):
        self.get_grid_nodes()
        self.get_to_starting_position()
        self.get_node_connections()
        for t in range(trips):
            for m in range(population):
                self.one_ant()
                self.calculate_tau_update()
                
                #Adding Tau updates to Tau, clearing Tau_updates
                for row in self.nodes:
                    for node in row:
                        if len(node.previous_node) > 0:
                            node.previous_node = (node.previous_node[0], (1-0.4)*node.previous_node[1] + node.previous_node[2], 0)
                        if len(node.next_node) > 0:
                            node.next_node = (node.next_node[0], (1-0.4)*node.next_node[1] + node.next_node[2], 0)


                

        
       
    def find_path(self):
        final_path_node = self.nodes[self.height-1][self.width-1]
       
        path_node = final_path_node
        print("final distance at node {} is: {}, qith weight {}".format(path_node.node_position, path_node.distance, path_node.weight))
        path_node = path_node.previous_node[0]
      
        while len(path_node.previous_node) >0:
            print("The previous node is {} and has distance {}, and weight {}".format(path_node.node_position, path_node.distance, path_node.weight))
            path_node = path_node.previous_node[0]
            
            
######################

my_ACO = ACO(100, 100)
my_ACO.go(30,40)


accuracy_sum = [1 for x in my_ACO.end_nodes if x == (99,99)]
accuracy_sum = sum(accuracy_sum)/len(my_ACO.end_nodes)
accuracy_sum
#as we can see this algorithm doesn't work


