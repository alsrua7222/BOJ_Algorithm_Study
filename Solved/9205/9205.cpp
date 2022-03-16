// 풀이 과정
// https://blog.naver.com/alsrua7222/222674491040

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
int N;
pair<int, pi> arr[103];
vector<int> Graph[103];
int visited[103];
string BFS() {
    queue<int> Queue;
    Queue.push(0);
    visited[0] = 1;
    
    while (!Queue.empty()) {
        int cur = Queue.front();
        Queue.pop();

        rep(0, Graph[cur].size()) {
            if (visited[Graph[cur][i]]) continue;
            if (Graph[cur][i] == N + 1) return "happy";
            visited[Graph[cur][i]] = 1;
            Queue.push(Graph[cur][i]);
        }
    }
    return "sad";
}
int getDistance(pi a, pi b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}
void initialize() {
    memset(visited, 0, sizeof(visited));
    rep(0, 103) {
        Graph[i] = vector<int>();
    }
    return;
}
int main()
{
	BOOST;
    int t; cin >> t;
    while (t--) {
        initialize();
        cin >> N;
        cin >> arr[0].second.first >> arr[0].second.second;
        rep(1, N + 1) {
            arr[i].first = i;
            cin >> arr[i].second.first >> arr[i].second.second;
            for (int j = 0; j < i; j++) {
                if (getDistance(arr[j].second, arr[i].second) <= 1000) {
                    Graph[arr[j].first].push_back(arr[i].first);
                    Graph[arr[i].first].push_back(arr[j].first);
                }
            }
        }
        arr[N + 1].first = N + 1;
        cin >> arr[N + 1].second.first >> arr[N + 1].second.second;
        for (int j = 0; j <= N; j++) {
            if (getDistance(arr[j].second, arr[N + 1].second) <= 1000) {
                Graph[arr[j].first].push_back(arr[N + 1].first);
                Graph[arr[N + 1].first].push_back(arr[j].first);
            }
        }
        cout << BFS() << "\n";
    }
    return 0;
}
