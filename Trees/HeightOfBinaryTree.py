#Height of a Binary Tree
#            10        Level1
#           / \
#          20  30      Level2
#         / \  / \
#        40 50 N  60   Level3
#            \
#            80        Level 4

#Height = Total Levels = 4
root=TreeNode(10)
root.left=TreeNode(20)
root.left.left=TreeNode(40)
root.right=TreeNode(30)
root.right.right=TreeNode(60)
root.left.right=TreeNode(50)
root.left.right.right=TreeNode(80)

def heightoftree(root):
    if root==None:
        return 0
    return 1+max(heightoftree(root.left),heightoftree(root.right))
heightoftree(root)
