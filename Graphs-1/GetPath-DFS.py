# prolem statement- we have to print the path between two given vertices using the DFS (Depth First Search) Algorithm

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

    def containsEdge(self,v1,v2):
        if self.adjMatrix[v1][v2]!=0:
            return True
        else:
            return False

    def getPathDFShelper(self,sv,ev,visited):
        if sv==ev:
            path=[ev]
            return True,path
        visited[sv]=True
        for i in range(self.vertices):
            if self.adjMatrix[sv][i]==1 and visited[i]==False:
                hasPath,path=self.getPathDFShelper(i,ev,visited)
                if hasPath==True:
                    path.append(sv)
                    return True,path
        return False,[]
        
            

    def getPathDFS(self,sv,ev):
        visited=[False for i in range(self.vertices)]
        hasPath,path=self.getPathDFShelper(sv,ev,visited)
        if hasPath==True:
            return path
        return list()


# main
v,e=map(int,input().split())
if v>0 and e>0:
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int,input().split())
        g.addEdge(v1,v2)
    sv,ev=map(int,input().split())
    path=g.getPathDFS(sv,ev)
    for i in path:
        print(i,end=" ")