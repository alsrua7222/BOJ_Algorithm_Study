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
 
ll n, q, x;
ll prefixSum[200001], prefixMax[200001];
 
int solve() {
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> x;
        prefixSum[i] = prefixSum[i - 1] + x;
        prefixMax[i] = max(prefixMax[i - 1], x);
    }
 
    for (int i = 1; i <= q; i++) {
        cin >> x;
        cout << prefixSum[upper_bound(prefixMax + 1, prefixMax + 1 + n, x) - prefixMax - 1] << " ";
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