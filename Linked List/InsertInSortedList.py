'''
Given a sorted singly linked list and a data, your task is to insert the data in the linked list in a sorted way i.e. order of the list doesn't change.

Example 1:

Input:
LinkedList: 25->36->47->58->69->80
data: 19
Output: 19 25 36 47 58 69 80
Example 2:

Input:
LinkedList: 50->100
data: 75
Output: 50 75 100
Your Task:
The task is to complete the function sortedInsert() which should insert the element in sorted Linked List and return the head of the linked list

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 104
-99999 <= A[i] <= 99999, for each valid i
'''



#User function Template for python3

def sortedInsert(head1,key):
    temp=head1
    newnode=Node(key)
    flag=1
    #if head is greater than key
    if key<temp.data:
        newnode.next=temp
        return newnode

    #if we have to insert in between
    curr=temp
    t1=temp
    while temp.next:
        prev=curr
        curr=curr.next
        if curr.data>key:
            prev.next=newnode
            newnode.next=curr
            flag=0
            return t1
        temp=temp.next
    #if no node is greater than key insert at the end/tail
    if flag==1:
        temp.next=newnode
    return t1
