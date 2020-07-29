'''
Add 1 to a number represented as linked list 
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Input:
The First line contains the number of test cases, and for each test case a single line of input denotes an big number N.

Output:
For each test case, print the resulting number in a new line.

User Task:
Your task is to complete the function addOne() which takes the head of the linked list as the only argument and returns the head of the modified linked list. The driver code prints the number and adds a new line.
Note: The head represents the left-most digit of the number.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 101000

Example:
Input:
4
456
123
999
1879
Output:
457 
124 
1000 
1880
Explanation:
456 + 1 = 457
123 + 1 = 124
999 + 1 = 1000
1879 + 1 = 1880
'''
#Python 3

def reverse(head):
# this function reverses the linked list
    prev = None
    current = head
    next = head.next
    
    while current is not None:
        next = current.next       # storing next node
        current.next = prev       # linking current node to previous
        prev = current            # updating prev
        current = next            # updating current
    
    return prev

def addOne(head):
    head = reverse(head)          # reversing list to make addition easy
    
    current = head
    carry = 1
    
    while(carry):
        current.data += 1         # adding one to current node
        
        if current.data < 10:
            return reverse(head)
            # if no carry we can reverse back list and return it
        else:
            current.data = 0
            # else we continue with taking carry forward
        
        if current.next is None:
            break
            # if end of list, we break from loop
        else:
            current = current.next
            # else we move to next node
    
    current.next = Node(1)        # adding new node for the carried 1
    return reverse(head)