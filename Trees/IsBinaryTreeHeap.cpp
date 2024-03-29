/*
Is Binary Tree Heap 

Given a binary tree you need to check if it follows max heap property or not.

Input:
The task is to complete the method which takes one argument, root of Binary Tree. The struct Node has a data part which stores the data, pointer to left child 
and pointer to right child.There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should return true if property holds else false.
 

Constraints:
1 <=T<= 30
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

Example:
Input:
2
2
5 2 L 5 3 R
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
1
0

There are two test cases.  First case represents a tree with 3 nodes and 2 edges where root is 5, left child of 5 is 2 and right child of 5 is 3.   Second test case represents a tree with 4 edges and 5 nodes.

*/


/*
 A binary tree node has data, pointer to left child
   and a pointer to right child 
struct Node
{
    int data;
    Node* left;
    Node* right;
};
*/

/*You are required to complete this method */
bool isHeap(Node * root)
{
 // Your code here
    if (root==NULL) return true;
    if ((root->left !=NULL && root->data < root->left->data) || (root->right !=NULL && root->data < root->right->data)){
        return false;
    }
    return isHeap(root->left) && isHeap(root->right);
    
 
}
