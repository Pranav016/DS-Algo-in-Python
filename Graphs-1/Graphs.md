# Graphs-
1. Adjacent vertices-  If two vertices are connected through the same edge then they are called adjacent vertices.

1. Degree of a vertex- The number of edges connected to that vertex is called the Degree of that vertex.

1. Path- The path needed to cover from one node to reach another if called Path.

1. Connected Graph- When there exist a path between any two vertices in a graph then it is called a Connected Graph.

1. Connected Component/ Island- Different connected graphs in one whole graph.

1. Tree- A graph which is always connected and does not have any cycle is called a tree.


### Min Edges in a graph = 0

### Min edges in a Connected graph having n vertices = n-1

### Max edges in a connected graph having n vertices = (n)*(n-1)*(n-2)*(n-3)....(1)
### = (n*(n-1))/2
### = O(n^2) which is the worst case complexity for any operation along the edge.


# Storing the GRAPH-

## Adjacency list- For an adjacency list we can make a hashmap for each vertex as a key and all its adjacent vertices as its values.

## Adjacency matrix- We can store our graph in a n X n Adjacency matrix of zero's. For each pair of nodes having an edge, we put 1 at position of the indexes in the adjacency martix