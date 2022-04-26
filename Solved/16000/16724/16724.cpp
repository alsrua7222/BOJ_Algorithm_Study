#include <iostream> // min, max, stdio
#include <algorithm> // sort
#include <vector> // default data struct
#include <cmath> // pow, sqrt, ceil, floor
#include <sstream> // for string
#include <string> // string methods
#include <queue> // queue, priority_queue
#include <deque> // deque
#include <utility> // pair
#include <unordered_map> // hash_map (<hash_map> lib is not used, cuz will be delete lib.)
#include <set>
using namespace std;

int N, M;
int cnt = 0;
vector<string> map;
vector<vector<bool>> visited;
void DFS(int x, int y) {
	queue<pair<int, int>> Queue;
	Queue.push({ x, y });
	set<pair<int, int>> goal;
	int X, Y;
	while (!Queue.empty()) {
		X = Queue.front().first;
		Y = Queue.front().second;
		Queue.pop();
		if (visited[Y][X]) {
			auto it = goal.find({ X, Y });
			if (it != goal.end()) {
				cnt++;
				return;
			}
			else {
				return;
			}
		}
		goal.insert({ X, Y });
		visited[Y][X] = true;
		if (map[Y][X] == 'D') Queue.push({ X, ++Y });
		else if (map[Y][X] == 'U') Queue.push({ X, --Y });
		else if (map[Y][X] == 'L') Queue.push({ --X, Y });
		else Queue.push({ ++X, Y });

	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		string s; cin >> s;
		map.push_back(s);
	}
	visited.assign(N, vector<bool>(M, false));
	for (int col = 0; col < N; col++) {
		for (int row = 0; row < M; row++) {
			if (visited[col][row]) continue;
			DFS(row, col);
		}
	}
	cout << cnt;
	return 0;
}