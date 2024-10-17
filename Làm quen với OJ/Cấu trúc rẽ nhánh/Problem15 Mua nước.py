n, a, b = map(int, input().split())
if(b / 2 >= a): # b / 2 là tính nước trên 1 l của b 
    print(a * n)
else:
    if(n % 2 == 0):
        print(n // 2 * b)
    else: print((n - 1) // 2 * b + a)

"""
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, a, b;
    cin >> n >> a >> b;
    vector<int> F(n + 1, INT_MAX);
    F[0] = 0; 
    for (int i = 1; i <= n; i++) {
        if (i >= 1) {
            F[i] = min(F[i], F[i - 1] + a);
        }
        if (i >= 2) {
            F[i] = min(F[i], F[i - 2] + b);
        }
    }
    cout << F[n];
    return 0;
}
"""