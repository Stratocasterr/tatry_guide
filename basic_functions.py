from tkinter import W
import numpy as np
from hmac import new
from operator import ne
from os import remove
from textwrap import indent
from tracemalloc import start
import numpy as np 
import pygame
from config import *
from text import *
from colors import *


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
    is_string = False
    name = ''
    pname = ''

    for point in points:
        
        #
        if type(point) == str: pname = point
        else: pname = point.name  
        for letter in pname:
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



def draw_the_line(path, points, points_names, offset_x, offset_y):
    cords = []
    for step in path[0]:
        for point_name in points_names:
            if point_name == step:
                cords.append([points[points_names.index(point_name)].x + offset_x, points[points_names.index(point_name)].y + offset_y])

    # input for line to draw points = [(x1, y1), (x2, y2), ..., (xn, yn)]

    for i in range(len(cords)):
        if i < len(cords) - 1:
           
            pygame.draw.line(WIN, PURPLE, cords[i], cords[i+1], 8)
                
def draw_info(point, offset_x, offset_y):
    pygame.draw.rect(WIN, OFF_WHITE, pygame.Rect(
        point.x - 2 * point.radius + offset_x,
        point.y + 5 * point.radius + offset_y,
        8 * len(point.name), 5 * point.radius))

    text_rendering(point.name, MENU_GREEN, OFF_WHITE, (point.x + offset_x - 2 * point.radius + (8 * len(point.name)) / 2, point.y + offset_y + 5 * point.radius + (5 * point.radius) / 2), BASIC_FONT)

def check_point_collision(point, offset_x, offset_y):
    rect = pygame.Rect(point.x + offset_x, point.y + offset_y, 3 * point.radius, 3 *  point.radius)
    if rect.collidepoint(pygame.mouse.get_pos()):
        return True
    else : return False

def draw_help_info(button, x, y):
    info = ''
    if button == "from":
        info = 'wfnojwrfjowrnfjwr fwrnojfnwrfjwr fwrnofwrnjfwrfnp'
    elif button == "to":
        info = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzzzzzzzzzzzzz'

    pygame.draw.rect(WIN, OFF_WHITE,
                    pygame.Rect(x + 600, y, 100,100))

def animate_arrow(counter):
# animate arrowR
    pygame.draw.polygon(WIN, LIGHT_GREEN, [(295, 327), (310, 339), (310, 315)])
    pygame.draw.rect(WIN,LIGHT_GREEN,
                    pygame.Rect(310, 321, 20, 12))

# animate arrowL
    pygame.draw.polygon(WIN, LIGHT_GREEN, [(160, 327), (145, 339), (145, 315)])
    pygame.draw.rect(WIN,LIGHT_GREEN,
                    pygame.Rect(125, 321, 20, 12))

    counter+=1
    if counter > 150:
        # animate arrowR
        pygame.draw.rect(WIN,MENU_GREEN,
                    pygame.Rect(295, 315, 35, 25))

        # animate arrowL
        pygame.draw.rect(WIN,MENU_GREEN,
                    pygame.Rect(125, 315, 40, 25))

        if counter == 200: counter = 0
    return counter

def find_name(points_names, input_name):
    suggestions = []
    if len(input_name) > 0:
        for point in points_names:
            if point[:len(input_name)] == input_name:
                if not (any(char.isdigit() for char in point)): suggestions.append(point)
                 
    return suggestions


def draw_suggestions(suggestions):
    pygame.draw.rect(WIN, OFF_WHITE,
                    pygame.Rect(110,345,145,len(suggestions) * 15))

    offset_y = 0
    for sug in suggestions:
        text_rendering(sug, MENU_GREEN, OFF_WHITE, (180, 350+ offset_y,), BASIC_FONT)
        offset_y += 15


def prettier_path(path, caps_lock_points, available_points):
    pretty_path = [[],path[1]]
    
    for step in path[0]:
        pretty_path[0].append(convert(caps_lock_points[available_points.index(step)]))

    return pretty_path

def convert(string):
    string = string.lower()
    for s in range(len(string)-1): 
        if string[s] == " ": string = string[:s+1] + string[s+1].upper() + string[s+2:]
    string = string[0].upper() + string[1:]
    return string



def draw_details(path):
    print(len(path[0]))
    height = 0
    if len(path[0]) <= 5 : height = len(path[0]) * 26
    else: height = len(path[0]) * 17
    pygame.draw.rect(WIN, OFF_WHITE,
                    pygame.Rect(10 ,315 ,180,height))

    text_rendering("Distance " + "      m", MENU_GREEN, OFF_WHITE, (100, 330), CRAZY_FONT)
    text_rendering(": " + str(path[1]), MENU_GREEN, OFF_WHITE, (118, 330), BASIC_FONT)
    offset_y = 0
    for index,step in enumerate(path[0]):
        text_rendering(str(index + 1) + ". " + step, MENU_GREEN, OFF_WHITE, (100, 345+ offset_y,), BASIC_FONT)
        offset_y += 15
