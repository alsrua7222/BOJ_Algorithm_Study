#pragma once
#include <iostream> // min, max, stdio
#include <algorithm> // sort
#include <vector> // default data struct
#include <cmath> // pow, sqrt, ceil, floor
#include <sstream> // for string
#include <string> // string methods
#include <queue> // queue, priority_queue
#include <deque> // deque
#include <utility> // pair
#include <cstring>
#include <unordered_map> // hash_map (<hash_map> lib is not used, cuz will be delete lib.)
#include <set> // sorted set
#include <map> // sorted map
#include <stack> // stack
#include <random>
#include <unordered_set>
//#include "berlekamp_massey.h"
using namespace std;
#define BOOST ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define rep(x,y) for(int i = x; i < y; i++)
typedef long long ll;
typedef pair<int, int> pi;
 
int q;
int solve() {
    cin >> q;
    map<char, int> dict[3];
    for (int i = 0, d, k; i < q; i++) {
        bool pass = false;
        int flag = 0;
        string str;
        cin >> d >> k >> str;
 
        for (char j : str) dict[d][j] += k;
 
        char ch = 'a';
        for (int j = 0; j < 26; j++) {
            for (int k = j + 1; k < 26; k++) {
                if (dict[1][ch + j] && dict[2][ch + k]) {
                    cout << "YES" << "\n";
                    pass = true;
                    break;
                }
            }
            if (pass) break;
        }
        if (pass) continue;
 
        for (int j = 0; j < 26; j++) {
            if (dict[1][ch + j]) {
                flag++;
                for (int k = 0; k < j; k++) {
                    if (dict[2][ch + k]) {
                        cout << "NO" << "\n";
                        pass = true;
                        break;
                    }
                }
            }
            if (pass) break;
        }
        if (pass) continue;
        if (flag >= 2) {
            cout << "NO" << "\n";
        }
        else {
            for (int j = 0; j < 26; j++) {
                if (dict[1][ch + j]) {
                    if (dict[1][ch + j] >= dict[2][ch + j]) {
                        cout << "NO" << "\n";
                    }
                    else {
                        cout << "YES" << "\n";
                    }
                    pass = true;
                    break;
                }
            }
            if (!pass) cout << "YES" << "\n";
        }
 
    }
    
    // cout << "\n";
    return 0;
}
int main() {
    BOOST;
    int t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}