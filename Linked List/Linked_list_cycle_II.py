'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# return type-node

#APPROACH 1 -Naive

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None:          #if list is empty return none
            return None
        s=set()                 #create a set
        while head.next!=None:
            if head in s:       #if node is already in the set then it's a loop
                return head
            s.add(head)
            head=head.next
        return None
#APPROACH 2 -Optimistic


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=fast=temp=head
        flag=False
        if head==None:
            return None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                flag=True
                break
        if flag==False:
            return None
        
        while temp!=fast:
            temp=temp.next
            fast=fast.next
        return fast
