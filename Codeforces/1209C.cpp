#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <algorithm>

template<typename datatype>
bool contains(const datatype &vec, int val) {
    return vec.size() > 0 && find(vec.begin(), vec.end(), val) != vec.end();
}

std::string process(std::string origInput, std::vector<int> ds) {
    std::deque<int> less, greater;
    if (ds.size() == 1)
        return "1";
    std::vector<int> uniq;
    for (int i : ds) {
        if (!contains(uniq, i))
            uniq.push_back(i);
    }
    if (uniq.size() == 1)
        return std::string(ds.size(), '1');
    if (uniq.size() == 2) {
        int a,b;
        if (uniq[0] <= uniq[1]) {
            a = uniq[0];
            b = uniq[1];
        } else {
            a = uniq[1];
            b = uniq[0];
        }
        std::string newString;
        for (int i : ds) {
            newString += (i == a) ? '1' : '2';
        }
        return newString;
    }
    int firstIneqIndex=-1, firstIneqLow, firstIneqHigh, firstIneqMoving;
    int lastIneqIndex=ds.size(), lastIneqLow, lastIneqHigh;
    int lessMax, lessMin, greaterMax, greaterMin;
    for (int e = 0; e < ds.size()-1; e++) {
        int j = ds[e];
        int i = ds[e+1];
        if (j > i) {
            if (firstIneqIndex == -1) {
                firstIneqIndex = e;
                firstIneqLow = firstIneqMoving = i+1;
                firstIneqHigh = j;
            }
            if (!contains(less, i)) {
                if (less.size() > 0 && i < lessMax)
                    return "-";
                less.push_back(i);
                if (i > lessMax)
                    lessMax = i;
                if (i < lessMin)
                    lessMin = i;
            }
            if (!contains(greater, j)) {
                if (greater.size() > 0 && j < greaterMax)
                    return "-";
                greater.push_back(j);
                if (j > greaterMax)
                    greaterMax = j;
                if (j < greaterMin)
                    greaterMin = j;
            }
            lastIneqIndex = e;
            lastIneqLow = i;
            lastIneqHigh = j;
        }
    }
    if (firstIneqIndex >= 0) {
        for (int _i = 0; _i < firstIneqIndex; _i++) {
            int i = ds[_i];
            if (i > firstIneqHigh)
                return "-";
            else if (i >= firstIneqMoving) {
                if (greater.size() == 0 || std::find(greater.begin(), greater.end(), i) == greater.end()) {
                    greater.push_back(i);
                }
                if (i > greaterMax)
                    greaterMax = i;
                if (i < greaterMin)
                    greaterMin = i;
                firstIneqMoving = i;
            }
            else if (i >= firstIneqLow)
                return "-";
        }
    }
    for (int _i = lastIneqIndex + 2; _i < ds.size(); _i++) {
        int i = ds[_i];
        if (i < lastIneqLow)
            return "-";
        else if (i < lastIneqHigh) {
            if (less.size() == 0 || std::find(less.begin(), less.end(), i) == less.end()) {
                less.push_back(i);
            }
            if (i > lessMax)
                lessMax = i;
            if (i < lessMin)
                lessMin = i;
            lastIneqLow = i;
        }
    }
    if (less.size() == 0 && greater.size() == 0)
        return std::string(ds.size(), '1');
    if (lessMax > greaterMin)
        return "-";
    sort(less.begin(), less.end());
    sort(greater.begin(), greater.end());
    bool currentLessFound=false, currentGreaterFound=false;
    int mostRecent_1 = 0, first_2 = 10;
    std::string s = "";
    for (int i : ds) {
        // cout<<s<<" ";
        // for (int l : less) cout<<","<<l;
        // cout<<" ";
        // for (int g : greater) cout<<","<<g;
        // cout<<endl;
        if (i < less[0] && !currentLessFound) {
            s += "1";
            mostRecent_1 = i;
            less.push_front(i);
            currentLessFound = true;
            continue;
        }
        if (currentLessFound && i >= less[less.size()-1] && i < greater[0] && !currentGreaterFound) {
            s += "2";
            if (first_2 > 9)
                first_2 = i;
            greater.push_front(i);
            currentGreaterFound = true;
            continue;
        }

        auto greaterFind = find(greater.begin(), greater.end(), i);
        if (greaterFind != greater.end()) {
            auto greaterPos = greaterFind - greater.begin();
            if (greaterPos == 0) {
                s += "2";
                if (first_2 > 9)
                    first_2 = i;
                currentGreaterFound = true;
                continue;
            }
            else if (greaterPos == 1 && currentGreaterFound) {
                s += "2";
                if (first_2 > 9)
                    first_2 = i;
                currentGreaterFound = true;
                greater.pop_front();
                continue;
            }
        }
        auto lessFind = find(less.begin(), less.end(), i);
        if (lessFind != less.end()) {
            auto lessPos = lessFind - less.begin();
            if (lessPos == 0) {
                s += "1";
                mostRecent_1 = i;
                currentLessFound = true;
                continue;
            }
            else if (lessPos == 1 && currentLessFound) {
                s += "1";
                mostRecent_1 = i;
                currentLessFound = true;
                less.pop_front();
                continue;
            }
        }

        if (currentGreaterFound && greater[0] < i && greater.size() > 1 && i < greater[1]) {
            s += "2";
            if (first_2 > 9)
                first_2 = i;
            currentGreaterFound = true;
            greater[0] = i;
        }
        else if (currentLessFound && less[0] < i && less.size() > 1 && i < less[1]) {
            s += "1";
            mostRecent_1 = i;
            currentLessFound = true;
            less[0] = i;
        }
        else if (currentGreaterFound && greater[0] < i && greater.size() == 1) {
            s += "2";
            if (first_2 > 9)
                first_2 = i;
            currentGreaterFound = true;
            greater[0] = i;
        }
        else if (currentLessFound && less[0] < i && less.size() == 1) {
            s += "1";
            mostRecent_1 = i;
            currentLessFound = true;
            less[0] = i;
        }
        else
            return "-";
        
        if (mostRecent_1 > first_2)
            return "-";
    }
    return s;
}

int main() {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int m;
        std::cin >> m;
        std::string s;
        std::cin >> s;
        std::vector<int> ds;
        for (char c : s) {
            ds.push_back(c-'0');
        }
        std::cout << process(s, ds) << std::endl;
    }
}
