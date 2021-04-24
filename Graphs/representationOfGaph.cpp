#include<stdio.h>
#include<bits/stdc++.h>
#include<iostream>

using namespace std;

vector<pair<int , int>>adjList[100100];
int adjMat[1001][1001];  //adjMat[i][j] cost of edge i->j 

int main(){
    int n, m; //number of vertices and edges
    
    cin >> n >> m;
    
    for (int i=0; i<m; i++){
        int u, v, w;
        cin >> u >> v >> w;
        //there is an edge u --> v of weight w
    
        adjList[u].push_back(make_pair(v, w));

        adjMat[u][v] = w;
    }
}
