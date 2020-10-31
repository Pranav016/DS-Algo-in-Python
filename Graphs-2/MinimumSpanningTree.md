# Minimum Spanning Tree:
For a weighted, undirected graph, a MST is a graph who's all vertices are connected without any cycles with the minimum total edge weight possible.
* There will be total n vertices and (n-1) edges in a minimum spanning tree.

## Kruskal's Algorithm:
Acc to Kruskal-
* Start selecting edges with the minimum weight.
* If the edge is forming a cycle then do not include it.
* We can stop when we get total n-1 edges.

## Detecting cycles-
* Detecting cycles is a huge part of kruskal's algorithm, one way to do it is to check if for any two vertices v1 and v2 already have a path between them. If they already have a path between them, then we will not include this new minimum weight edge.
* This approach takes approx O(n^2) complexity which is very large hence we have to come up with a better approach.

## Union Find Algorithm: