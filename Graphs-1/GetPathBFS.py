import queue


class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adjMatrix=[[0 for j in range(self.vertices)]for i in range(self.vertices)]

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

    def __str__(self):
        return str(self.adjMatrix)

    def bfsHelper(self,sv,ev,visited,path):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while not q.empty():
            cur=q.get()
            for i in range(self.vertices):
                if self.adjMatrix[cur][i]>0 and visited[i] is False:
                    path[i]=cur
                    if i==ev:
                        print(ev,end=" ")
                        return True
                    q.put(i)
                    visited[i]=True


    def bfs(self,sv,ev):
        visited=[False for j in range(self.vertices)]
        path=dict()
        if self.bfsHelper(sv,ev,visited,path) is True:
            return path
        return dict()
            


# main
v,e=map(int,input().split())
if v>0 and e>0:
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int,input().split())
        g.addEdge(v1,v2)
    sv,ev=map(int,input().split())
    path=g.bfs(sv,ev)
    x=path.get(ev,-1)
    while x!=-1:
        print(x,end=" ")
        x=path.get(x,-1)