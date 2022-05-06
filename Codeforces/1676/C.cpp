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

int main() {
    BOOST;
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int ans = 1;
        int a[100100], b[100100], c[100100], vis[100100];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        map<int, int>cnt;
        for (int i = 0; i < n; i++) {
            cin >> b[i];
        }

        for (int i = 0; i < n; i++) {
            cin >> c[i];
        }

        set<int>s;
        for (int i = 0; i < n; i++) {
            s.insert(i + 1);
            cnt[a[i]] = i;
            vis[i] = 0;
        }

        while (s.size()) {
            auto it = s.begin();
            bool k = 0;
            int p = *it;
            while (1) {
                s.erase(p);
                if (c[cnt[p]]) {
                    k = 1;
                }
                vis[cnt[p]] = 1;
                int o = b[cnt[p]];
                if (p == o) {
                    k = 1;
                    break;
                }
                if (vis[cnt[o]]) {
                    break;
                }
                else {
                    p = o;
                }
            }
            if (k == 0) {
                ans *= 2;
                ans %= 1000000007;
            }
        }
        cout << ans << endl;
    }
    return 0;
}