'''
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''




class Solution:
    queue=[]
    def pushneibhours(self,pair,matrix,r,c):
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        p1=pair[0]
        p2=pair[1]
        for i in range(4):
            nodex=p1+x[i]
            nodey=p2+y[i]
            if nodex<0 or nodey<0 or nodex>=r or nodey>=c or matrix[nodex][nodey]!=1:
                continue
            self.queue.append((nodex,nodey))
            matrix[nodex][nodey]=2
                
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        time=0
        #queue=[]   #store all rotten oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    self.queue.append((i,j))
        total=len(self.queue)
        while total>0:
            for i in range(total):
                pair=self.queue.pop(0)#nei=exist+1 hai to push it in queue
                self.pushneibhours(pair,grid,row,col)
            total=len(self.queue)
            if total >0:
                time+=1    
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return -1
        return time
        
