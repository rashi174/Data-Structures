'''
#Better solution

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        res=''
        while l1 and l2:
            temp=l1.val+l2.val+carry
            carry=0
            if temp>=10:
                carry=1
                res+=str(temp%10)
            else:
                res+=str(temp)
            l1=l1.next
            l2=l2.next
        if l1 or l2:
            while l1:
                temp=l1.val+carry
                carry=0
                if temp>=10:
                    carry=1
                    res+=str(temp%10)
                else:
                    res+=str(temp)
                l1=l1.next
            while l2:
                temp=l2.val+carry
                carry=0
                if temp>=10:
                    carry=1
                    res+=str(temp%10)
                else:
                    res+=str(temp)
                l2=l2.next
        if carry==1:
            res+='1'
        root=ListNode(res[0])
        rootnext=root
        i=1
        while res and i<len(res):
            rootnext.next=ListNode(res[i])
            i+=1
            
            rootnext=rootnext.next
        return root
