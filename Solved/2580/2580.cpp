// 풀이 과정
// https://blog.naver.com/alsrua7222/222634634258

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
int arr[9][9];
int numbers[10];
vector<pair<int, int>> blank;

void entire_check(int x, int y) {
    for (int i = 1; i <= 9; i++) numbers[i] = i;
    for (int i = 0; i < 9; i++) numbers[arr[x][i]] = 0;
    for (int i = 0; i < 9; i++) numbers[arr[i][y]] = 0;
    int tmp_x = x - x % 3, tmp_y = y - y % 3;
    for (int i = tmp_x; i < tmp_x + 3; i++) {
        for (int j = tmp_y; j < tmp_y + 3; j++) {
            numbers[arr[i][j]] = 0;
        }
    }
    return;
}

bool backtracking(int cur) {
    if (cur == blank.size()) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) cout << arr[i][j] << " ";
            cout << "\n";
        }
        exit(0);
        return true;
    }

    int x = blank[cur].first;
    int y = blank[cur].second;
    for (int i = 1; i < 10; i++) {
        entire_check(x, y);
        if (numbers[i] == 0) continue;
        arr[x][y] = i;
        if (backtracking(cur + 1)) return true;
        arr[x][y] = 0;
    }
    return false;
}
int main()
{
    BOJSetting();
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 0) blank.push_back({ i, j });
        }
    }
    backtracking(0);
	return 0;
}
