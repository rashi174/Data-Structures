'''

Detect cycle in an undirected graph 

Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 

Example 1:

Input:   

Output: 1
Explanation: 1->2->3->4->1 is a cycle.

Example 2:

Input: 

Output: 0
Explanation: No cycle in the graph.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not.
 

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
 

Constraints:
1 ≤ V, E ≤ 105
'''

class Solution:
	def dfs(self,adj,vis,v,start,parent):
	    vis[start]=True
	    for node in adj[start]:
	        if vis[node]==False:
	            if self.dfs(adj,vis,v,node,start)==True:
	                return True
	        elif node!=parent:
	            return True
	    return False
	def isCycle(self, v, adj):
		vis=[False] * v
		for i in range(v):
		    if vis[i]==False:
		        if self.dfs(adj,vis,v,i,-1):
		            return True
		return False
