'''
#https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5'''

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        vec = list()
        while head != None:
            vec.append(head.val)
            head = head.next
        vec.sort(reverse=True)
        head = ListNode(0)
        head_copy = head
        while vec:
            head.next = ListNode(vec.pop())
            head = head.next
        return head_copy.next