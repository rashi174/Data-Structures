'''
637. Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:

The range of node's value is in the range of 32-bit signed integer.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def levelorder(root):
            result=[]
            if root==None: return result
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
            return result
        result=levelorder(root)
        res=[sum(i)/len(i) for i in result]
        return res[::-1]
