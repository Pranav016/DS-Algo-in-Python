# implementation of Graph class
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
        return
    
    def containsEdge(self,v1,v2):
        return self.adjMatrix!=0

    def __str__(self): # overloading the print method
        return str(self.adjMatrix)

    def dfsHelper(self,sv,visited):
        print(sv)
        visited[sv]=True
        for j in range(self.vertices):
            if self.adjMatrix[sv][j]==1 and visited[j]==False:
                self.dfsHelper(j,visited)

    def dfs(self):
        visited=[False for j in range(self.vertices)]
        self.dfsHelper(0,visited)

    def bfsHelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while not q.empty():
            cur=q.get()
            print(cur,end=" ")
            for i in range(self.vertices):
                if self.adjMatrix[cur][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True


    def bfs(self):
            visited=[False for j in range(self.vertices)]
            for i in range(self.vertices):
                if visited[i] is False:
                    self.bfsHelper(i,visited)

# main
v,e=map(int,input().split())
if v>0 and e>0:
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int,input().split())
        g.addEdge(v1,v2)
    g.bfs()