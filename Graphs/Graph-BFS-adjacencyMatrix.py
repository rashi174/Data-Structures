
#Implementation of graph using adjacency matrix and BFS traversal

class Graph:
  adj=[]  #declaring adj matrix

  def __init__(self,v,e):
    self.v=v
    self.e=e
    Graph.adj=[[0 for i in range(v)] for j in range(v)]
  
  def addedge(self,start,end):
    #considering bidirectional edge
    Graph.adj[start][end]=1
    Graph.adj[end][start]=1

  def bfs(self,start):
    visited=[False] * self.v
    queue=[start]
    visited[start]=True

    while queue:
      node=queue.pop(0)
      print(node,end=" ")
      for i in range(self.v):
        if Graph.adj[node][i]==1 and not visited[i]:
          queue.append(i)
          visited[i]=True

#driver code

# Driver code
v, e = 5, 4

# Create the graph
G = Graph(v, e)
G.addedge(0, 1)
G.addedge(0, 2)
G.addedge(1, 3)

# Perform BFS
G.bfs(0)
