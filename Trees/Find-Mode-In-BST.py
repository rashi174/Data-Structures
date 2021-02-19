'''
501. Find Mode in Binary Search Tree
Easy

1228

400

Add to List

Share
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        def inorder(root):
            list1=[]
            if root:
                list1.extend(inorder(root.left))
                list1.append(root.val)
                list1.extend(inorder(root.right))
            return list1
        inorderlist=inorder(root)
        dict1={}
        
        for i in inorderlist:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        res=[]
        m=max(dict1.values())
        for i in dict1.keys():
            if dict1[i]==m:
                res.append(i)
        return res
        
