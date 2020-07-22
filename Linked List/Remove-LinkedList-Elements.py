#https://leetcode.com/problems/remove-linked-list-elements/
'''
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return head
        curr=head
        prev=None
        while curr!=None:
            if curr.val==val:
                if prev==None:  #head node is to be deleted
                    head=head.next
                    curr=head
                else:
                    prev.next=curr.next
                    curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return head