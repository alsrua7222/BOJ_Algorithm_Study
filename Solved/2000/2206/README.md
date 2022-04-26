# 벽 부수고 이동하기

## 해결 과정
### 0. 처음에는 2차원으로 풀려고 시도를 해봤으나, 파이썬, C++로 다 TLE이 나왔다.
시도는 처음에 0,0에서 N,M까지 가는 길에 벽의 위치를 다 수집하도록 했다.    
벽의 위치를 하나씩 받으면서 지우고 BFS로 탐색돌고 다시 채우고 그런 식으로 했다.   
당연히 TLE 떴다.   

2번째 시도는 0,0에서 N,M까지 BFS탐색하다가 벽을 만나면 방문한 기록, 현재 정보들을 넘겨주고 DFS를 탐색한다. N,M를 도달하면 리턴 값은 길이 값이고, 아니라면 -1로 받게 된다.   
-1이라면 잠깐 멈췄던 BFS를 다시 시작했다.    
하지만 방문한 기록들을 넘기는 과정이 깊은 복사를 계속 하는 바람에 TLE가 떴다.    
### 1. 결국 2차원 방법으로 해결하려는 것을 포기하고 3차원으로 세워서 풀었다.
쉽게 풀었다.   
```C++
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
```
