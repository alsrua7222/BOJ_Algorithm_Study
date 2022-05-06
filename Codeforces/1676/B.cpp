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
//#include "berlekamp_massey.h"
using namespace std;
#define BOOST ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define rep(x,y) for(int i = x; i < y; i++)
typedef long long ll;
typedef pair<int, int> pi;

int n;
vector<ll> a;
void solve() {
    cin >> n;
    string s; cin >> s;
    set<char> dict;
    int k; cin >> k;
    for (int i = 0; i < k; i++) {
        char ch; cin >> ch;
        dict.insert(ch);
    }

    int cur = -1, MAX = -1;
    for (int i = n - 1; i >= 0; i--) {
        if (dict.find(s[i]) == dict.end()) {
            if (cur == -1) continue;
            cur++;
            MAX = max(MAX, cur);
        }
        else {
            MAX = max(MAX, cur + 1);
            cur = 0;
        }
    }

    if (MAX == -1) {
        cout << "0\n";
    }
    else {
        cout << MAX << "\n";
    }
    return;
}

int main()
{
    BOOST;
    int t; cin >> t;
    while (t--) {
        solve();
    }
    
    
    return 0;
}
