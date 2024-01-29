#include <iostream>
#include <string>
#include <list>
#include <sstream>

using namespace std;

int main()
{
    string s;
    cin >> s;
    list<char> new_s;
    list<char>::iterator idx = new_s.begin();
    for (char& c : s)
    {
        switch (c)
        {
            case 'L':
                idx--;
                break;
            case 'R':
                idx++;
                break;
            case 'B':
                idx--;
                idx = new_s.erase(idx);
                break;
            default:
                new_s.insert(idx, c);
        }
    }
    
    stringstream str;
    for (char& c : new_s)
    {
        str << c;
    }
    cout << str.str() << endl;
}
