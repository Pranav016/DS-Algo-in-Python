# Kruskal's algorithm helps us to find the minimum spanning tree.
# Time complexities- e.log(e) + e*v


class Edge:
    def __init__(self,src,dest,wt):
        self.src=src
        self.dest=dest
        self.wt=wt

def getParent(v,parent):
    if v==parent[v]:
        return v
    return getParent(parent[v],parent)


def Kruskal(edges,vertices):
    parent=[int(i) for i in range(vertices)]
    edges = sorted(edges,key = lambda edge: edge.wt)
    count=0

    output=[]
    i=0
    while count < vertices-1:
        currentEdge=edges[i]
        srcParent=getParent(currentEdge.src,parent)
        destParent=getParent(currentEdge.dest,parent)
        if srcParent!=destParent:
            output.append(currentEdge)
            count+=1
            parent[srcParent]=destParent
        i+=1
    return output



# main
v,e=map(int,input().split())
edges=[]
for i in range(e):
    lst=[int(i) for i in input().split()]
    src=lst[0]
    dest=lst[1]
    wt=lst[2]
    edge=Edge(src,dest,wt)
    edges.append(edge)
output=Kruskal(edges,v)
for edge in output:
    if edge.src < edge.dest:
        print(str(edge.src)+" "+str(edge.dest)+" "+str(edge.wt))
    else:
        print(str(edge.dest)+" "+str(edge.src)+" "+str(edge.wt))