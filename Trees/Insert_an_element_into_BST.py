''''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 
'''

#Insert an element into a BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root==None:   #if tree is empty the make the given val as root of the tree and return 
            root=TreeNode(val)
            return root
        if val<root.val:   #recursively check if value is less than root than add in left subtree
            root.left=self.insertIntoBST(root.left,val)
        else: 
            root.right=self.insertIntoBST(root.right,val)
        #finally return the updated Binary Search tree
        return root
        
