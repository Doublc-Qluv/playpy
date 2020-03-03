#include<iostream>
#include<queue>
using namespace std;
int ans, n;
priority_queue<int> pq;
int main(){
    cin >> n;
    for(int i = 1, x;i <=n ;i++){
        cin >> x;
        pq.push(-x);
    }

    
    while (pq.size() > 1){
        int x = pq.top();
        pq.pop();
        x += pq.top();
        pq.pop();
        pq.push(x);
        ans -= x;
    }
    cout << ans;
    return 0;
}