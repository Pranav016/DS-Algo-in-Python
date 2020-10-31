# problem statement- we have to return all the different sub-graphs (disconnected graphs) within the given graph

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

    def dfsHelper(self,sv,visited,main):
        small=[]
        visited[sv]=True
        small.append(sv)
        for i in range(self.vertices):
            if self.adjMatrix[sv][i]==1 and visited[i]==False:
                lst=self.dfsHelper(i,visited,main)
                for i in lst:
                    small.append(i)
        return small    
        

    def dfs(self):
        visited=[False for i in range(self.vertices)]
        main=[]
        for i in range(self.vertices):
            if visited[i]==False:
                main.append(self.dfsHelper(i,visited,main))
        return main
                
            

# main
v,e=map(int,input().split())
if v>0 and e>0:
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int,input().split())
        g.addEdge(v1,v2)
    main=g.dfs()
    for lst in main:
        lst.sort()
        for j in lst:
            print(j,end=" ")
        print()