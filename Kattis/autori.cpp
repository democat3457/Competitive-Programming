#include <iostream>

using namespace std;

int main()
{
    string jon;
    string doc;
    cin >> jon >> doc;
    if (jon.length() >= doc.length())
    {
        cout << "go";
    }
    else
    {
        cout << "no";
    }
}