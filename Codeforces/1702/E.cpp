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
bool visited[200020];
ll N, cnt;
void DFS(map<ll, set<ll>> & mp2, ll cur, ll parent) {
    if (visited[cur]) return;

    visited[cur] = true;
    cnt++;

    for (auto it = mp2[cur].begin(); it != mp2[cur].end(); it++) {
        if (*it == parent) continue;
        if (visited[*it]) continue;

        DFS(mp2, *it, cur);
    }
    return;
}

string solve() {
    cin >> N;
    map<ll, ll> mp;
    map<ll, set<ll>> mp2;

    bool success = true;
    for (int i = 0; i < N; i++) {
        ll a, b; cin >> a >> b;
        mp[a]++;
        mp[b]++;

        if (a == b) success = false;
        
        mp2[a].insert(b);
        mp2[b].insert(a);
    }

    for (auto it : mp) {
        if (it.second != 2) {
            success = false;
            break;
        }
    }

    if (success == false) return "NO";

    memset(visited, false, sizeof(visited));
    
    for (int i = 1; i <= N; i ++) {
        cnt = 0;
        if (visited[i] == false) DFS(mp2, i, -1);
        if (cnt % 2) {
            success = false;
            break;
        }
    }
    if (success) return "YES";
    else return "NO";
}
int main() {
    BOOST;
    int t; cin >> t;
    while (t--) {
        cout << solve() << "\n";
    }
    return 0;
}