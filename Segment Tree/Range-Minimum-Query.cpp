/*
Range Minimum Query 

Given an array A[ ] and its size N your task is to complete two functions  a constructST  function which builds the segment tree  and a function RMQ which finds range minimum query in a segment tree .

Input:
The task is to complete two functions constructST and RMQ .
The constructST function builds the segment tree and takes two arguments the array A[ ] and the size of the array N .
It returns a pointer to the first element of the segment tree array . 
The RMQ function takes 4 arguments the first being the segment tree st constructed, second being the size N and then third and forth arguments are the range of query a and b .The function RMQ returns the min of the elements in the array from index range a and b. There are multiple test cases. For each test case, this method will be called individually.

Output:
The function RMQ should return the min element in the array from range a to b .

Constraints:
1<=T<=100
1<=N<=10^3+1
1<=Q(no of queries)<=10000
0<=a<=b

Example:
Input (To be used only for expected output) 
1 
4
1 2 3 4
2
0 2 2 3

Output
1 3

Explanation
1. For query 1 ie 0 2 the element in this range are 1 2 3 and the min element is 1  
2. For query 2 ie 2 3 the element in this range are 3 4 and the min element is 3 

*/

void construction(int node,int start,int endd,int *arr,int *st){
    if (start==endd) {  //terminating condition (only single node)
        st[node]=arr[start];
        return; 
    }
    int mid=(start+endd)/2;
    construction(node*2,start,mid,arr,st); //Left Subtree
    construction(node*2+1,mid+1,endd,arr,st);  //right subtree
    st[node]=min(st[node*2],st[node*2+1]);   //minimum of left and right child
}


int *constructST(int arr[],int n)
{
    int *st = new int[4*n];  
    construction(1,0,n-1,arr,st);
    return st;
    
}

int query(int node,int start,int endd,int left,int right,int *st){
    if(start > right || endd < left){
        return INT_MAX;
    }
    
    if(start >= left && endd <= right){
        return st[node];
    }
 
    int mid;
    mid = (start+endd)/2;
    int x = query(2*node,start,mid,left,right,st);
    int y = query(2*node+1,mid+1,endd,left,right,st);
 
    return min(x,y);
    
}
int RMQ(int st[] , int n, int a, int b)
{
    return query(1,1,n,a+1,b+1,st);
}
