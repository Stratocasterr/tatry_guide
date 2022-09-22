# Dijkstra's Algorithm

Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph.
It differs from the minimum spanning tree because the shortest distance between two vertices might not include all the vertices of the graph.

![image](https://user-images.githubusercontent.com/101999487/190897365-15dfaf32-ad8e-4e27-a1fa-7ac10ad1a6e2.png)

## How Dijkstra's Algorithm works

Dijkstra's Algorithm works on the basis that any subpath B -> D of the shortest path A -> D between vertices A and D is also the shortest path between vertices B and D.
Djikstra used this property in the opposite direction i.e we overestimate the distance of each vertex from the starting vertex. Then we visit each node and its neighbors to find the shortest subpath to those neighbors.

The algorithm uses a greedy approach in the sense that we find the next best solution hoping that the end result is the best solution for the whole problem.

info source : https://www.programiz.com/dsa/dijkstra-algorithm
read about Dijkstra in PL: https://eduinf.waw.pl/inf/alg/001_search/0138.php
drawings: Kacper Wolański