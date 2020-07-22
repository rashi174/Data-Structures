'''
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
'''

#Approach 1 --------->  o(n) runtime & o(n) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s=set()  #set to store the addresses of the nodes
        while head!=None:  #loop unitl head!=None (end of linkedlist)
            if head in s:   #check if head already in s
                return True   #if so then a loop exists 
            s.add(head)      #else add address to the set
            head=head.next   #increment the head pointer
        return False       #after loop ends there is no loop found in list
        