# problem statement- We have to check if all the graph nodes are connected or not

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

    def bfsHelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while not q.empty():
            cur=q.get()
            for i in range(self.vertices):
                if self.adjMatrix[cur][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True


    def bfs(self):
        visited=[False for j in range(self.vertices)]
        self.bfsHelper(0,visited)
        for i in range(self.vertices):
            if visited[i]==False:
                return False
        return True
            

# main
v,e=map(int,input().split())
if v>0 and e>0:
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int,input().split())
        g.addEdge(v1,v2)
    if g.bfs():
        print("true")
    else:
        print("false")