import numpy as np
from hmac import new
from operator import ne
from os import remove
from textwrap import indent
from tracemalloc import start
import numpy as np 
import basic_functions


# Dijkstra's main algorithm
def the_shortest_path(A,B,graph):

    # basic Dijkstra init
    S=[]
    Q=graph[2].copy()
    d=np.full(len(Q),float('inf'))
    d[Q.index(A)]=0
    p=np.full(len(Q),'none').tolist()
    start=0
    

    while len(Q)>0:

        # min weight from elements in Q
        start=np.amin(basic_functions.cut_d(d,S,graph)).astype(int)

        # D-array index of min weight from elements in Q
        vertex=[np.where(d==start)][0][0]
        
        # check if there are a few elements with the same weight
        if len(vertex)>1:
            for i in vertex:
                if graph[2][i] not in S:
                    vertex=i
        else: vertex=vertex[0]

        S.append(graph[2][vertex])
        Q.remove(graph[2][vertex])

        neighbours=basic_functions.find_neighbours(S[-1],graph)
        print(S[-1])
        for nei in neighbours:
            weight=basic_functions.find_weight_btwn_neighbours(S[-1],nei,graph)
            #print(weight,nei)

            if d[graph[2].index(nei)]>int(d[graph[2].index(S[-1])])+int(weight):
                d[graph[2].index(nei)]=int(d[graph[2].index(S[-1])])+int(weight) 
                p[graph[2].index(nei)]=S[-1]

    
    print("S ",S)
    print("Q: ",Q)
    print("D: ",d)
    print("P: ",p)
    print("####################################")
    
    
    # building answer  [path (list of vertices), total weight of path]
    answer=[B]
    # building path
    while answer[-1]!=A:
        answer.append(p[graph[2].index(answer[-1])])

    # building total weight of path
    weight=int(d[graph[2].index(B)])
    return [basic_functions.upstdn_array(answer),weight]
