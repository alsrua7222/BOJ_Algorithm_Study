// 풀이 과정
// https://blog.naver.com/alsrua7222/222631966302

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
using namespace std;
void BOJSetting() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}
int N, i, j, k;
vector<int> korea, western;

int custom_bs(vector<int>& arr1, vector<int>& arr2) {
    int left = 0, right = i + 1;
    while (left < right) {
        int mid = (left + right) / 2;
        int X = k - mid;
        if ((1 <= X && X <= j && arr2[X] <= arr1[mid]) || X <= 0) right = mid;
        else left = mid + 1;
    }
    return right;
}

int main()
{
    BOJSetting();
    cin >> N;
    korea.assign(N + 2, 0);
    western.assign(N + 2, 0);
    for (int idx = 1; idx <= N; idx++) cin >> korea[idx];
    for (int idx = 1; idx <= N; idx++) cin >> western[idx];

    int Q; cin >> Q;
    while (Q--) {
        cin >> i >> j >> k;
        int right = custom_bs(korea, western);
        int cnt = (int)(upper_bound(western.begin() + 1, western.begin() + j + 1, korea[right]) - western.begin() - 1);
        if ((right != i + 1) && (cnt == k - right)) cout << 1 << ' ' << right << "\n";
        else {
            swap(i, j);
            right = custom_bs(western, korea);
            cout << 2 << ' ' << right << "\n";
        }
    }
	return 0;
}
