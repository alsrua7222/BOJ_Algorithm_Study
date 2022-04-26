# �Ǹ� �δ� �糪��
https://www.acmicpc.net/problem/16724
## �ذ� ����
### 0. Union Find�� �ذ��� �� �ְ�, DFS�� �ذ��� �� �ִ�.
### 1. DFS�� Union-Find���� ��������, �������� �ſ� ���� �����ϴµ� �� ������.
�׷���, �ǹ̰� DFS����, �׳� �ܹ��⼺�� ������ �ִ� Ư���� �ֱ� ������ �̴� DFS�� ������ ��� ȣ��� ���� ���ذ� �� ���̴�.		
���� BFS�� ������ ���� �־���.		
�� ����ϰ� ��ȯó���ϰ� ���� ���� BFS ������ ������ �����ߴ�.		
### 2. ���� ���� �߿��� �׻� ��ǥ�踦 ��Ż�ϴ� ��찡 ���ٰ� �ϴϱ�, ����ó���� ���ص� �ȴ�.
### 3. �ʱ� ������ �Ʒ��� ����.
```c++
visited.assign(N, vector<bool>(M, false));
for (int col = 0; col < N; col++) {
	for (int row = 0; row < M; row++) {
		if (visited[col][row]) continue;
		DFS(row, col);
	}
}
```
N * M ��ŭ ��ȸ�ϸ鼭 �湮 ó������ ���� ��ġ��, DFS Ž���ϵ��� �����Ѵ�. �ʱ� �湮ó���� DFS���� ó���Ѵ�.
### 4. DFS ����鼭 ���� ���ǿ� ���� �߰� �����ϰ�, ������.
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
DFS �ڵ�� ���� ����.		

```c++
queue<pair<int, int>> Queue;
Queue.push({ x, y });
set<pair<int, int>> goal;
int X, Y;
```

�̴� DFS �����ϱ� ���� �ʱ� ���� �����ϴ� ���̴�.		
goal ������ ������ �ڸ��� ����Ŭ�� �����ߴ��� üũ�ϱ� ���� �뵵��.		

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
�湮 ó���Ǿ� ������ �̹� ����Ŭ(�ݺ� ����)�� ���ԵǾ� �ִ��� �ƴϸ� ���ο� ����Ŭ�� ���ԵǾ� �ִ��� üũ�Ѵ�.		
�̰��� ��ǻ� ���� �б����� �ǹ��ϴ� ���̶� ����. �׷��� else ������ �� �ʿ䰡 ������.			
ť�� �����ϸ鼭 ����� �ؽ����̺� ������ ����Ŭ ������ �ƴ��� �Ǵ��� �� �ִ�.		
```c++
goal.insert({ X, Y });
visited[Y][X] = true;
if (map[Y][X] == 'D') Queue.push({ X, ++Y });
else if (map[Y][X] == 'U') Queue.push({ X, --Y });
else if (map[Y][X] == 'L') Queue.push({ --X, Y });
else Queue.push({ ++X, Y });
```
�湮 ó���Ǿ� ���� ������ �ؽ����̺� ����Ŭ ����� �ϰ� �湮 ó���� �ϰ� ���� ��ġ�� ���� ���� ���� �༱���� ť�� �����Ų��.		
�����ϴ�.

�Ƹ´�. �̹� �湮 ó���� �������� ���ο� ����Ŭ�� ���Եȴٸ� cnt�����ϴ� ���� �����ٵ�, �̴� �������� cnt�� �����ϸ� ���ϰ� ����� �� �ִ�.		

### 5. DFS �� ���� �������� cnt�� ����Ѵ�.