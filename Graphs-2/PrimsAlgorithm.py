# This algorithm helps us to find the minimum spanning tree by exploring all the adjacent vertices of the current vertex and connecting it to the one having minimum edge weight.
# Time complexity is O(n^2)

import queue
import sys


class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adjMatrix=[[0 for j in range(self.vertices)]for i in range(self.vertices)]

    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2]=wt
        self.adjMatrix[v2][v1]=wt

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

    def get_minVertex(self,visited,weight):

        min_vertex=-1
        for i in range(self.vertices):
            if visited[i] is False and (min_vertex==-1  or weight[min_vertex]>weight[i]):
                min_vertex=i
        return min_vertex

    def Prims(self):
        visited=[False for i in range(self.vertices)]
        parent=[-1 for i in range(self.vertices)]
        weight=[sys.maxsize for i in range(self.vertices)]
        for i in range(self.vertices-1):
            min_vertex=self.get_minVertex(visited,weight)
            visited[min_vertex]=True
        
        # explore the neibhors of the vertex which is not visited
        # update the weight corresponding to them if required

        for j in range(self.vertices):
            if self.adjMatrix[min_vertex][j]>0 and visited[j] is False:
                if weight[j]>self.adjMatrix[min_vertex][j]:
                    weight[j]=self.adjMatrix[min_vertex][j]
                    parent[j]=min_vertex

        for i in range(1,self.vertices):
            if i<parent[i]:
                print(str(i)+" "+str(parent[i])+" "+str(weight[i]))
            else:
                print(str(parent[i])+" "+str(i)+" "+str(weight[i]))

# main
v,e=map(int,input().split())
g=Graph(v)
for i in range(e):
    lst=[int(i) for i in input().split()]
    g.addEdge(lst[0],lst[1],lst[2])
g.Prims()