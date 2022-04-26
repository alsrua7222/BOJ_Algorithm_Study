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
using namespace std;
typedef struct info {
	int x;
	int y;
	int value;
}info;

int N, M;

vector<string> map;
vector<vector<bool>> visited;

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

void BFS() {
	int node, x, y, value, X, Y;
	queue<info> Queue;
	Queue.push({0, 0, 1});
	
	while (!Queue.empty()) {
		x = Queue.front().x;
		y = Queue.front().y;
		value = Queue.front().value;
		Queue.pop();
		if (x + 1 == M && y + 1 == N) { cout << value; break; }
		for (int i = 0; i < 4; i++) {
			X = x + dx[i];
			Y = y + dy[i];
			if (0 <= X && X < M && 0 <= Y && Y < N) {
				if (visited[Y][X]) continue;
				if (map[Y][X] == '1') {
					visited[Y][X] = true;
					Queue.push({X, Y, value + 1});
				}
			}
		}
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N >> M;
	visited = vector<vector<bool>>(N, vector<bool>(M, false));
	for (int i = 0; i < N; i++) {
		string s; cin >> s;
		map.push_back(s);
	}
	
	visited[0][0] = true;
	BFS();

	return 0;
}