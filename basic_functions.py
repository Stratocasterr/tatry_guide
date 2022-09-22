import numpy as np
from hmac import new
from operator import ne
from os import remove
from textwrap import indent
from tracemalloc import start
import numpy as np 



def graph_check(graph):

    #check the graph representation 
    if type(graph[0])!=type(s): raise Exception("Invalid type of adjacency matrix!")
    if type(graph[1])!=type(s): raise Exception("Invalid type of weights matrix!")
    if type(graph[2])!=list: raise Exception("Invalid type of vertex list!")
    print("Correct graph representation")
        
    #check if graph is 2D matrix
    if len(graph[1].shape)!=2: raise Exception("Invalid weights matrix dimension!")
    if len(graph[0].shape)!=2: raise Exception("Invalid adjacency matrix dimension!")
    if graph[0].shape[0]!=graph[0].shape[1]: raise Exception("Invalid adjacency matrix shape!")
    if graph[1].shape[0]!=graph[1].shape[1]: raise Exception("Invalid weights matrix shape!")
    print("Correct graph dimension")    
    


    #Does the adjacency matrix contain only 0/1?
    n = graph[0].flatten()
    for i in range(0, len(n)):
        if n[i] != 1 and n[i] != 0:
            raise Exception("Invalid adjacency matrix values!")    
    print("Correct adjacency matrix values")

    
    #Do the connection-weight matrix and connection matrix have the same dimension?
    if graph[1].shape!=graph[0].shape: raise Exception("Weights matrix and connection matrix have different dimensions!")
        
   
    #Check node amount
    if len(graph[2])!=len(graph[0]): raise Exception("Invalid graph's nodes amount")
    print("Correct graph's nodes amount")
    print("Your graph is fully correct!")

def remove_node(graph,node_to_remove):
    if node_to_remove in graph[2]:
        s=graph[2].index(node_to_remove)
        graph[0] = np.delete(graph[0], s, axis=0)
        graph[0] = np.delete(graph[0], s, axis=1)
        graph[1] = np.delete(graph[1], s, axis=0)
        graph[1] = np.delete(graph[1], s, axis=1)
        graph[2].remove(node_to_remove)
        print("Node: ",node_to_remove," removed.")
        print("The remaining nodes: ", graph[2])
        return
    else:
        raise Exception("Invalid node")

def add_node(graph,node_to_add):
    graph[2].append(node_to_add)
    graph[0]=np.concatenate((graph[0], np.zeros((1, graph[0].shape[1]))),axis=0)
    graph[0]=np.concatenate((graph[0], np.zeros((graph[0].shape[0], 1))),axis=1)
    graph[1]=np.concatenate((graph[1], np.zeros((1, graph[1].shape[1]))),axis=0)
    graph[1]=np.concatenate((graph[1], np.zeros((graph[1].shape[0], 1))),axis=1)

    graph[0]=graph[0].astype(int)
    graph[1]=graph[1].astype(int)
    
def add_connection(graph,node_1,node_2):
    graph[0][graph[2].index(node_1)][graph[2].index(node_2)]=1
    graph[0][graph[2].index(node_2)][graph[2].index(node_1)]=1

def remove_connection(graph,node_1,node_2):
    graph[0][graph[2].index(node_1)][graph[2].index(node_2)] = 0
    graph[0][graph[2].index(node_2)][graph[2].index(node_1)] = 0

def print_info(graph):
    for i in range(graph[0].shape[0]):
        for j in range(graph[0].shape[1]):
            if graph[0][i][j] == 1:
                if graph[2][i]==graph[2][j]:
                    continue
                else:
                    print("For node: ",graph[2][i]," neighbor is: ",graph[2][j]," weight of this connection: ",graph[1][i][j])

def print_neighbours(graph,node):
    
    neighbors=[]
    if node in graph[2]:
        ix=graph[0][graph[2].index(node)]
        for i in range(ix.size):
            if ix[i]==1:
                neighbors.append(graph[2][i])
        print("For node: ",node," neighbors are: ",neighbors)
    else:
        raise Exception("Invalid node!")

# dijkstra
def find_neighbours(A,graph):
    if A in graph[2]:
        answer=[]
        row=graph[0][graph[2].index(A)]
        for i in range(len(row)):
            if row[i]==1:
                answer.append(graph[2][i])
        return answer
    else:
        raise Exception("Invalid node name!")

def find_weight_btwn_neighbours(A,B,graph):
    return graph[1][graph[2].index(A)][graph[2].index(B)]
    
def cut_d(d,S,graph):
    new_d=d.copy()
    for i in range(len(d)):
        if graph[2][i] in S:
            new_d=np.delete(new_d,np.where(new_d==d[i])[0][0])
    return new_d

def upstdn_array(array):
    return [array[len(array)-x-1] for x in range(len(array))]



def get_points_names(points):
    answer = []
    
    name = ''
    for point in points:
        if not (any(char.isdigit() for char in point.name)):
           
            for letter in point.name:
                if letter == "Ż": name += 'z'
                elif letter == "Ń": name += 'n'
                elif letter == "Ó": name += 'o'
                elif letter == "Ś": name += 's'
                elif letter == "Ć": name += 'c'
                elif letter == "Ą": name += 'a'
                elif letter == "Ę": name += 'e'
                elif letter == "Ł": name += 'l'
                elif letter == "Ź": name += 'z'
                else : name += letter
            name = name.lower()
            
            answer.append(name)
            name = ''
    return answer

def find_point(point_name, points):
    for point in points:
        if point.name == point_name:
            return [point.x, point.y]

# input for line to draw points = [(x1, y1), (x2, y2), ..., (xn, yn)]
def draw_the_line(points):
    for i in range(len(points)):
        if i < len(points) - 2:
            pygame.draw.line(WIN, RED, points[i], points[i+1], 8)


def find_name(points_names, input_name):
    suggestions = []
    if len(input_name) > 0:
        for point in points_names:
            if point[:len(input_name)] == input_name: suggestions.append(point)
    return suggestions


