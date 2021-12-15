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
typedef struct info {
	int x, y, w, brake;
}info;
int N, M;
int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };
vector<string> arr;
vector<vector<vector<bool>>> visited;

int BFS_DFS() {
	queue<info> Queue;
	Queue.push({ 0, 0, 0, 0});
	
	while (!Queue.empty()) {
		info pos = Queue.front();
		Queue.pop();

		if (visited[pos.y][pos.x][pos.brake] == 1) continue;
		visited[pos.y][pos.x][pos.brake] = 1;
		if (pos.y == N - 1 && pos.x == M - 1) {
			return pos.w + 1;
		}
		for (int i = 0; i < 4; i++) {
			int X = pos.x + dx[i];
			int Y = pos.y + dy[i];
			if (0 <= X && X < M && 0 <= Y && Y < N) {
				if (arr[Y][X] == '1' && pos.brake) continue;
				int B = (arr[Y][X] - '0') + pos.brake;
				if (visited[Y][X][B]) continue;
				Queue.push({ X, Y, pos.w + 1, B });
			}
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	visited.assign(N, vector<vector<bool>>(M, vector<bool>(3, false)));

	for (int i = 0; i < N; i++) {
		string tmp; cin >> tmp;
		arr.push_back(tmp);
	}
	cout << BFS_DFS();
	
	return 0;
}
