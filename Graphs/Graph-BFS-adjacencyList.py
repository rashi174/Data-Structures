from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph=defaultdict(list)
  
  def addEdge(self,u,v):
    self.graph[u].append(v)  #adding edges bw the nodes
  
  def bfs(self,s):  # s is the starting node from where bfs will beginnnnn :)
    visited=[False] * (max(self.graph)+1)
    queue=[s]  
    visited[s]=True
    while queue:
      node=queue.pop(0)
      print(node,end=" ")
      for i in self.graph[node]:
        if visited[i]==True:
          pass
        else:
          queue.append(i)
          visited[i]=True
          
#driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

#calling the bfs function
g.bfs(1)
