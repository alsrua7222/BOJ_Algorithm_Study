# 피리 부는 사나이
https://www.acmicpc.net/problem/16724
## 해결 과정
### 0. Union Find로 해결할 수 있고, DFS로 해결할 수 있다.
### 1. DFS가 Union-Find보다 느리지만, 가독성은 매우 좋고 이해하는데 더 빠르다.
그러나, 의미가 DFS이지, 그냥 단방향성을 가지고 있는 특성이 있기 때문에 이는 DFS와 유사한 재귀 호출로 보면 이해가 될 것이다.		
또한 BFS로 구현할 수도 있었다.		
난 깔끔하게 반환처리하고 보기 좋게 BFS 형식을 빌려서 구현했다.		
### 2. 문제 조건 중에서 항상 좌표계를 이탈하는 경우가 없다고 하니까, 예외처리를 안해도 된다.
### 3. 초기 셋팅은 아래와 같다.
```c++
visited.assign(N, vector<bool>(M, false));
for (int col = 0; col < N; col++) {
	for (int row = 0; row < M; row++) {
		if (visited[col][row]) continue;
		DFS(row, col);
	}
}
```
N * M 만큼 순회하면서 방문 처리되지 않은 위치면, DFS 탐색하도록 시작한다. 초기 방문처리는 DFS에서 처리한다.
### 4. DFS 만들면서 문제 조건에 따라 추가 구현하고, 돌린다.
```c++
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
```
DFS 코드는 위와 같다.		

```c++
queue<pair<int, int>> Queue;
Queue.push({ x, y });
set<pair<int, int>> goal;
int X, Y;
```

이는 DFS 시행하기 전에 초기 변수 설정하는 것이다.		
goal 변수는 지나간 자리에 싸이클이 존재했는지 체크하기 위한 용도다.		

```c++
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
```
방문 처리되어 있으면 이미 싸이클(반복 패턴)에 포함되어 있는지 아니면 새로운 싸이클에 포함되어 있는지 체크한다.		
이것은 사실상 종료 분기점을 의미하는 것이랑 같다. 그래서 else 블럭문을 열 필요가 없었다.			
큐에 적재하면서 기록한 해쉬테이블에 존재한 싸이클 값인지 아닌지 판단할 수 있다.		
```c++
goal.insert({ X, Y });
visited[Y][X] = true;
if (map[Y][X] == 'D') Queue.push({ X, ++Y });
else if (map[Y][X] == 'U') Queue.push({ X, --Y });
else if (map[Y][X] == 'L') Queue.push({ --X, Y });
else Queue.push({ ++X, Y });
```
방문 처리되어 있지 않으면 해쉬테이블에 싸이클 기록을 하고 방문 처리를 하고 현재 위치의 값에 따라 다음 행선지를 큐에 적재시킨다.		
간단하다.

아맞다. 이미 방문 처리된 시점에서 새로운 싸이클에 포함된다면 cnt증가하는 것을 봤을텐데, 이는 전역변수 cnt로 선언하면 편하게 계산할 수 있다.		

### 5. DFS 다 돌면 전역변수 cnt를 출력한다.