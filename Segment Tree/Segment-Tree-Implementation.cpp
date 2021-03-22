#include <iostream>
using namespace std;
 
int seg[400005];
int a[100005];
void construction(int node,int start, int endd);
int query(int node,int start, int endd, int left, int right);
int n;
int main()
{
    int left,right,q;
 
    cin >> n;
 
    for(int i = 1; i <= n; i++){
        cin >> a[i];
    }
 
    // why is it imp ??? 
    memset(seg,0,sizeof(seg));
 
    // node = 1, start = 1 ,endd = 5;
    construction(1,1,n);
 
    for(int i = 1; i <= 2*n; i++){
        cout << seg[i]<<endl;
    }
 
    cin >> q;
 
    while(q--){
        cin >> left >> right; 
 
        int ans = query(1,1,n,left,right);
 
        cout << ans << endl;
    }
}
 
void construction(int node,int start, int endd){
    
 
    if(start == endd){
        seg[node] = a[start];
        return ;
    }
 
    int mid = (start+endd)/2;
 
    // start == 1, endd == 2, node == x
    construction(2*node,start,mid);
    construction(2*node+1,mid+1,endd);
 
    // executing this line , its left and right child has some value
    seg[node] = seg[2*node] + seg[2*node+1];
 
    //cout << node <<" "<<start<<" "<<endd<<" "<<seg[node]<<endl;
}
 
int query(int node,int start, int endd, int left, int right)
{
 
    if(start > right || endd < left){
        return 0;
    }
    
    if(start >= left && endd <= right){
        return seg[node];
    }
 
    int mid;
    mid = (start+endd)/2;
    int x = query(2*node,start,mid,left,right);
    int y = query(2*node+1,mid+1,endd,left,right);
 
    return x+y;
}
