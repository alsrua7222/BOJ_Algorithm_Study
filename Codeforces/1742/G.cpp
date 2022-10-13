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

int n, a;
vector<pi> vt;
int solve() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        vt.push_back({ a, a });
    }
    int bit = 0;
    sort(vt.begin(), vt.end());
    for (int i = 0; i < n; i++) {
        cout << vt[vt.size() - 1].second << " ";
        bool flag = false;
        for (int j = 0; j < 30; j++) {
            if ((((bit >> j) & 1) == 0) && (((vt[vt.size() - 1].second >> j) & 1) == 1)) {
                for (int k = 0; k < vt.size(); k++) {
                    vt[k].first &= 2147483647 ^ (1 << j);
                }
                flag = true;
            }
        }
        bit |= vt[vt.size() - 1].second;
        vt.pop_back();
        if (flag) {
            sort(vt.begin(), vt.end());
        }
    }
    cout << "\n";
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