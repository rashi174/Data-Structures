'''
199. Binary Tree Right Side View



Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result=[]
        if root==None:
            return result
        queue=[]
        queue.append(root)
        while len(queue)>0:
            nodes=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                nodes.append(node.val)
                if node.left!=None:queue.append(node.left)
                if node.right!=None:queue.append(node.right)
            result.insert(0,nodes)
        res=[]
        for i in result:
            res.append(i[-1])
        return res[::-1]
