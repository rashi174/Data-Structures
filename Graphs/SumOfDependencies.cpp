//Given a directed graph with n nodes. If there is an edge from u to v then u depends on v. Our task is to find out the sum of dependencies for every node.
//https://practice.geeksforgeeks.org/problems/sum-of-dependencies-in-a-graph/0/?category[]=Graph&difficulty[]=-1&page=1&query=category[]Graphdifficulty[]-1page1#

#include <iostream>
using namespace std;

int main() {
	//code
	int t,n,e;
	cin>>t;
	while(t--)
	{
	cin>>n>>e;
	for(int i=0;i<e;i++)
	cin>>n>>n;
	cout<<e<<endl;
	}
	return 0;
}
