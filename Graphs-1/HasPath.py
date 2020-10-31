# sv = starting vertex and ev = ending vertex
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

    def hasPathHelper(self,sv,ev,visited):
        if self.adjMatrix[sv][ev]==1:
            return True
        visited[sv]=True
        for j in range(self.vertices):
            if self.adjMatrix[sv][j]==1 and visited[j]==False:
                if self.hasPathHelper(j,ev,visited)==True:
                    return True
                else:
                    continue
        return False


    def hasPath(self,sv,ev):
        visited=[False for i in range(self.vertices)]
        return self.hasPathHelper(sv,ev,visited)


# main
v,e=map(int,input().split())
if v>0 and e>0:
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int,input().split())
        g.addEdge(v1,v2)
    sv,ev=map(int,input().split())
    if g.hasPath(sv,ev):
        print("true")
    else:
        print("false")