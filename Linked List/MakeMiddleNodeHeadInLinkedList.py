'''
Make middle node head in a linked list
Given a singly linked list, find middle of the linked list and set middle node of the linked list at beginning of the linked list.

Examples:

Input  : 1 2 3 4 5 
Output : 3 1 2 4 5

Input  : 1 2 3 4 5 6
Output : 4 1 2 3 5 6 

The idea is to first find middle of a linked list using two pointers, first one moves one at a time and second one moves two at a time.
When second pointer reaches end, first reaches middle.
We also keep track of previous of first pointer so that we can remove middle node from its current position and can make it head.
'''

#linkedlist   1->2->3->4->5

temp=Node(1)
head=temp
temp.next=Node(2)
temp=temp.next
temp.next=Node(3)
temp=temp.next
temp.next=Node(4)
temp=temp.next
temp.next=Node(5)
temp=temp.next
temp.next=Node(6)

slow=fast=temp=head
while fast.next and fast.next.next:
    fast=fast.next.next
    slow=slow.next
print("Middle Value:",slow.data)

curr=temp
while curr.next:
    if curr==slow:
        prev.next=curr.next
    prev=curr
    curr=curr.next
slow.next=head
while slow:
    print(slow.data,end=" ")
    slow=slow.next
