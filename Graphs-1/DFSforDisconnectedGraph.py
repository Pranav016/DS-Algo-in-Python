class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adjMatrix=[[0 for j in range(vertices)]for i in range(vertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2):
            self.adjMatrix[v1][v2]=0
            self.adjMatrix[v2][v1]=0
        return

    def containsEdge(self,v1,v2):
        if self.adjMatrix[v1][v2]!=0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.adjMatrix)

    def dfsHelper(self,sv,visited):

        print(sv)
        visited[sv]=True
        for i in range(self.vertices):
            if self.adjMatrix[sv][i]==1 and visited[i]==False:
                self.dfsHelper(i,visited)
            

    def dfs(self):
        visited=[False for i in range(self.vertices)]
        for i in range(self.vertices):
            if visited[i]==False:
                self.dfsHelper(i,visited)


g=Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,3)
g.addEdge(0,2)
g.dfs()