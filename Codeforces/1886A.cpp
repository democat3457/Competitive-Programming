#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int t;
        cin >> t;
        if (t < 7) cout << "NO" << endl;
        else {
            int c = t - 3;
            if (c % 3 != 0 && c != 1 && c != 2)
                cout << "YES" << endl
                     << 1 << " " << 2 << " " << c << endl;
            else {
                c = t - 5;
                if (c % 3 != 0 && c != 1 && c != 4)
                    cout << "YES" << endl
                        << 1 << " " << 4 << " " << c << endl;
                else cout << "NO" << endl;
            }
        }
    }
}
