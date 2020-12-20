'''
Odd even level difference 

Given a Binary Tree. Find the difference between the sum of node values at even levels and the sum of node values at the odd levels.

Example 1:

Input:
            1
          /   \
         2     3

Output: -4

Explanation:
sum at odd levels - sum at even levels
= (1)-(2+3) = 1-5 = -4

Example 2:

Input:
            10
          /    \
        20      30
       /  \         
     40    60      

Output: 60

Explanation:
sum at odd levels - sum at even levels
= (10+40+60) - (20+30)
= 110 - 50
= 60

Your Task:  
You dont need to read input or print anything. Complete the function getLevelDiff() which takes root node as input parameter and returns an integer.
 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(height of tree)
 

Constraints:
1 ≤ N ≤ 10^5
'''




class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def getLevelDiff(root):
    queue=[root]
    ans=[]
    while (len(queue)>0):
        templ=[]
        for i in range(0,len(queue)):
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            templ.append(queue.pop(0).data)
        ans.append(templ)
    e=0 #even sum
    o=0 #odd sum
    for i in range(len(ans)):
        if i%2==0:
            o+=sum(ans[i])
        else:
            e+=sum(ans[i])
    return o-e
