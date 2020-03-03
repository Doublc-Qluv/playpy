#include <iostream>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <cstring>
#define ull unsigned long long
using namespace std;
ull n, k;
ull flag;
stack<ull> s;
int main() {
    cin >> n >> k;
    while(k) {
        s.push(k&1);
        k >>= 1;
    }
    for(int i = s.size()+1; i <= n; i++)
        cout << "0";
    while(!s.empty()) {
        ull current = s.top();
        s.pop();
        if(current != flag) cout << "1";
        else cout << "0";
        flag = current;
    }
    return 0;

    
}


/*

*/