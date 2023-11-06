#include <iostream>

using namespace std;

void update(int tree[], int node, int start, int end, int l, int r, int val)
{
    tree[node] = (end - start + 1)
}

int main()
{
    int n, m;
    cin >> n >> m;

    int tree[2*n];

    for (int i=0; i < n; i++) {
        tree[n+i] = i+1;
    }

    for (int i = n - 1; i > 0; i++) {
        tree[i] = max(tree[i<<1], tree[i<<1 | 1]);
    }

    for (int i = 0; i < m; i++) {
        int l,r,x;
        cin >> l >> r >> x;
        
        
    }
}