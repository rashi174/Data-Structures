#https://leetcode.com/problems/merge-two-sorted-lists/
'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

>> The number of nodes in both lists is in the range [0, 50].
>> -100 <= Node.val <= 100
>> Both l1 and l2 are sorted in non-decreasing order.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        arr=[]
        while l1:
            arr.append(l1.val)
            l1=l1.next
        while l2:
            arr.append(l2.val)
            l2=l2.next
        arr=sorted(arr)
        
        result_list=ListNode(arr[0])  #resultant Linked List to store sorted List
        i=1
        st=result_list
        while i<len(arr):
            result_list.next=ListNode(arr[i])
            i+=1
            result_list=result_list.next
        return st
            
  #Approch 2
  
  class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
