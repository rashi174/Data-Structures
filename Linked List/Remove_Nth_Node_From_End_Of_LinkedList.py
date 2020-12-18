#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
19. Remove Nth Node From End of List      (Medium)
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=head
        tummy=head #one more dummy
        counter=1
        
        while dummy:
            dummy=dummy.next
            counter+=1
        nth=counter-n-1
        if nth==0:
            return head.next
        
        i=1
        while tummy:
            if nth==i:  #1 1 # 2 2 # 33
                tummy.next=tummy.next.next
                return head
            i+=1
            tummy=tummy.next
        
                
                
        
        
