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
bool primes[100001];
bool wins[100001];
int prefixSum[100001];
vector<int> v;

void setPrimes() {
    for (int i = 2; i < sqrt(100001) + 1; i++) {
        if (primes[i]) continue;
        for (int j = i + i; j < 100001; j += i) {
            primes[j] = true;
        }
    }
    for (int i = 2; i < 100001; i++) {
        if (!primes[i]) v.push_back(i);
    }
    return;
}
void solve() {
    int A, k;
    cin >> A >> k;
    int cnt = 0, x = A + 1 - k;
    cnt = prefixSum[A] - prefixSum[A - k];
    int maxCnt = cnt, minX = x;
    x--;
    while (x >= 2) {
        if (!wins[x + k]) cnt--;
        if (!wins[x]) cnt++;
        if (cnt >= maxCnt) {
            maxCnt = cnt;
            minX = x;
        }
        x--;
    }
    cout << maxCnt << " " << minX << "\n";
}
int main() {
    BOOST;
    setPrimes();

    for (int i = 0; i < 100001; i++) {
        if (wins[i]) continue;
        for (int j = 0; j < v.size(); j++) {
            if (i + v[j] > 100000) break;
            wins[i + v[j]] = true;
        }
    }

    prefixSum[0] = 1;
    for (int i = 1; i < 100001; i++) prefixSum[i] = prefixSum[i - 1] + !wins[i];

    int t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}