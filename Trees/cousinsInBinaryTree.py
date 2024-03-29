'''
993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.parentx = -1
        self.parenty = -1
        self.levelx=-1
        self.levely=-1

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.helper(root,x,y)
        return self.parentx!=self.parenty and self.levelx==self.levely
        
    def helper(self,root,x,y):
        if root == None:
            return
        queue = [root]
        counter=0
        while queue:
            nodes=[]
            counter+=1
            for i in range(len(queue)):
                node=queue.pop(0)
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
                if node.left!=None and node.left.val==x:
                    self.parentx = node.val
                    self.levelx=counter
                if node.right!=None and node.right.val==x:
                    self.parentx = node.val
                    self.levelx=counter  
                if node.left!=None and node.left.val==y:
                    self.parenty = node.val
                    self.levely=counter   
                if node.right!=None and node.right.val==y:
                    self.parenty = node.val
                    self.levely=counter   
        

        
