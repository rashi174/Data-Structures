SEGMENT TREE:

The very first approach in this journey of answering queries is segment tree. It is one of the most powerful tree data structure which enables
us answering queries over an array successfully and also allows to modify the array at a single point or over a given segment. 
It is basically a binary tree which stores some segments.

Let’s consider an array A of length N and a segment tree T built over it
Root node of T will represent the whole array A [1, 2, …., N].
Each leaf node of T will represent a single array element A[i], 1<= i <=N.
Each internal node in T is responsible for a segment like A [l, l+1, l+2, …., r] 1 <= l, r <= N.

>> Structure of a general Segment Tree

Root node represents the whole array A [1: N]. We will break the array into two segments first A[1: (N+1)/2] and other A[ (N+1)/2+1 : N]. 
As it is a binary so each node has two children. First child of root will represent the segment A[1: (N+1)/2] and the second will represent
the segment A[(N+1)/2+1:N]. So, in each step we will split the segment into two halves and its two children will represent those halves.
We will keep splitting the segments till one node represents one array element.

![image](https://user-images.githubusercontent.com/51811507/112667233-07f09780-8e83-11eb-985d-f81d27512254.png)


-> Height of the Tree
Max height of the segment tree is ceil(log2(N)).

-> Size of Segment Tree (Space Complexity)
Total number of leaf nodes is at least N.
Total number of internal nodes = N-1.
So, total number of nodes = 2*N-1. But generally, to build a segment tree over an array of size N, we use a tree of 4*N nodes. (Why?)

->Array representation of above segment tree will be
Tree[]={1,2,3,4,5,6,7,8,9,dummy,dummy,10,11,dummy,dummy};
Since we use the array representation of the segment tree, so a bit space is wasted as you can see in above example. 
These waste space can be removed but in that case its implementation would be more complex. Considering these waste spaces, for smooth 
working of data structure, a tree of size 4*N is used, which is still of linear space complexity.

4*N size is enough for an array of size N. Why?

![image](https://user-images.githubusercontent.com/51811507/112667372-30789180-8e83-11eb-8e15-cc515c87d546.png)

A segment tree has only three operations

1.Building Tree : Initializing the segment tree variable and build its structure.
2.Updating Tree : Updating the value at a point or over an interval in the array and change tree accordingly.
3.Querying Tree : Answering accordingly.

