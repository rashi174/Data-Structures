'''     k-th smallest element in BST 


Given a BST and an integer K. Find the Kth Smallest element in the BST. 

Example 1:

Input:
      2
    /   \
   1     3
K = 2
Output: 2
Example 2:

Input:
        2
      /  \
     1    3
K = 5
Output: -1
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function KthSmallestElement() which takes the root of the BST and integer K as inputs and return the Kth smallest element in the BST, if no such element exists return -1.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1<=Number of nodes<=100000  '''

 


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Return the Kth smallest element in the given BST 
def KthSmallestElement(root, K): 
    #code here.
    inorder=[]
    if root==None:
        return -1
    def inorderTraversal(root):
        temp=[]
        if not root:
            return temp
        temp.extend(inorderTraversal(root.left))
        temp.append(root.data)
        temp.extend(inorderTraversal(root.right))
        return temp
    inorder=inorderTraversal(root)
    if len(inorder)<K:
        return -1
    return inorder[K-1]
