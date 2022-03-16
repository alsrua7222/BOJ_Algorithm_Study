// 풀이 과정
// https://blog.naver.com/alsrua7222/222674789723

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
vector<int> arr;

int main()
{
	BOOST;
    cin >> N;
    rep(0, N) {
        int tmp; cin >> tmp; arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end());
    int answer = 0, total = 0;
    rep(0, arr.size()) {
        total += arr[i];
        answer += total;
    }
    cout << answer;
    return 0;
}
