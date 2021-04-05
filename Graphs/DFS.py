class Solution:

  def dfs(self,graph,visited,start):
    visited[start]=True  #mark current node as visited
    print(start,end=' ') 
    for node in graph[start]:
      if visited[node]==False:
        self.dfs(graph,visited,node)
        visited[node]=True
  def mainfunction(self,graph):
    start=2  #starting point of DFS
    nodes=4  #total number of nodes
    visited=[False] * nodes   
    self.dfs(graph,visited,start)
    
graph={0:[1,2],2:[0,3],3:[3],1:[2]}
s1=Solution()
s1.mainfunction(graph)
