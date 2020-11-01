import sys
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
       
    
    def addEdge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
        
        
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
        
    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def printSolution(self, dist):
        for node in range(self.nVertices):
            print(node,dist[node])
    
	
    def minDistance(self, dist, sptSet): 
   
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
   
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.nVertices): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index 
   
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
   
        dist = [sys.maxsize] * self.nVertices 
        dist[src] = 0
        sptSet = [False] * self.nVertices 
   
        for i in range(self.nVertices): 
   
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
   
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
   
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.nVertices): 
                if self.adjMatrix[u][v] > 0 and sptSet[v]==False and  dist[v] > dist[u] + self.adjMatrix[u][v]:
                    
                    dist[v] = dist[u] + self.adjMatrix[u][v] 
   
        self.printSolution(dist) 
   

li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]

g = Graph(n)
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])
g.dijkstra(0)