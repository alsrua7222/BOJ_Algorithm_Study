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
	int m;
	int n;
	int h;
	int day;
}info;
int M, N, H;
int dx[] = { 1, 0, -1, 0, 0, 0 };
int dy[] = { 0, 1, 0, -1, 0, 0 };
int dz[] = { 0, 0, 0, 0, 1, -1 };
vector<vector<vector<int>>> map;
vector<vector<vector<bool>>> visited;

queue<info> init() {
	queue<info> result;
	for (int h = 0; h < H; h++) {
		for (int n = 0; n < N; n++) {
			for (int m = 0; m < M; m++) {
				if (map[h][n][m] == 1) {
					result.push({ m, n, h, 1 });
				}
			}
		}
	}
	return result;
}

int BFS() {
	int days = 1;
	queue<info> Queue = init();
	visited.assign(H, vector<vector<bool>>(N, vector<bool>(M, false)));

	int h, m, n, day, X, Y, Z;
	while (!Queue.empty()) {
		m = Queue.front().m;
		n = Queue.front().n;
		h = Queue.front().h;
		day = Queue.front().day;
		Queue.pop();

		if (days < day) days = day;
		for (int i = 0; i < 6; i++) {
			X = m + dx[i];
			Y = n + dy[i];
			Z = h + dz[i];
			if (0 <= X && X < M && 0 <= Y && Y < N && 0 <= Z && Z < H) {
				if (visited[Z][Y][X]) continue;
				if (map[Z][Y][X] == 0) {
					visited[Z][Y][X] = true;
					map[Z][Y][X] = day + 1;
					Queue.push({ X, Y, Z, day + 1 });
				}
			}
		}
	}
	return days - 1;
}

bool IsAllClear() {
	for (int h = 0; h < H; h++) {
		for (int n = 0; n < N; n++) {
			for (int m = 0; m < M; m++) {
				if (map[h][n][m] == 0) {
					return false;
				}
			}
		}
	}
	return true;
}

bool IsNotZero() {
	for (int h = 0; h < H; h++) {
		for (int n = 0; n < N; n++) {
			for (int m = 0; m < M; m++) {
				if (map[h][n][m] == 0) {
					return false;
				}
			}
		}
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> M >> N >> H;
	for (int h = 0; h < H; h++) {
		map.push_back(vector<vector<int>>(N, vector<int>(M)));
		for (int n = 0; n < N; n++) {
			for (int m = 0; m < M; m++) {
				cin >> map[h][n][m];
			}
		}
	}

	if (IsAllClear()) {
		cout << 0;
		return 0;
	}

	int result = BFS();


	if (IsNotZero()) {
		cout << result;
	}
	else {
		cout << -1;
	}
	return 0;
}
