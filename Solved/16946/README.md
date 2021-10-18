# 벽 부수고 이동하기 4
https://www.acmicpc.net/problem/16946
## 해결 과정
### 0. 평범한 BFS로 1를 찾아서 지날 수 있는 길의 길이를 증가하면서 적재시키면 안된다.
그 이유는 시간 초과가 나오기 때문이다.      
왜 그러냐면 지나간 길인데 또 이걸 지나가면서 카운트를 세는 것이다.      
그래서 메모이제이션 + 분리집합을 이용해서 적용시켜야 한다.       
### 1. 위의 해결 방안으로 다시 수정하면서 시도 한다.
```python
# 수정 전
arr = []
```
```python
# 수정 후
group_arr = [[0 for row in range(M)] for col in range(N)]
group_index_arr = [[0 for row in range(M)] for col in range(N)]
group_cnt = 2

result_map = []
```
수정하기 전에는 input받은 arr로 bfs를 탐색 시도 해봤지만 시간 초과로 터졌다.       
그래서 DP + 분리 집합 원리를 적용해서 맵을 더 추가했다.      
result_map은 arr의 문자를 쉽게 처리하기 위한 용도면서 출력 결과물을 담아낼 변수이다.      
### 2. setDP를 BFS로 운영하면서 지나간 위치를 기억한다.
```python
def setDP(x, y, visited):
    global group_cnt
    global group_arr

    Queue = deque()
    Queue.append([x, y])
    group_index_arr[y][x] = group_cnt
    answer = 1
    visited[y][x] = True

    # 지나간 자리에 지날 수 있는 최대 길이 값을 부여하기.
    index_q = deque()
    index_q.append([x, y])
    while Queue:
        tmpx, tmpy = Queue.popleft()
        for i in range(4):
            X = tmpx + dx[i]
            Y = tmpy + dy[i]
            if 0 <= X < M and 0 <= Y < N:
                if not visited[Y][X] and arr[Y][X] == '0' and group_arr[Y][X] == 0:
                    answer += 1
                    visited[Y][X] = True
                    group_index_arr[Y][X] = group_cnt
                    index_q.append([X, Y])
                    Queue.append([X, Y])

    while index_q:
        tmpx, tmpy = index_q.popleft()
        group_arr[tmpy][tmpx] = answer

    # 그룹 묶어주고 나서 1씩 증가해서 다음 그룹에 사용하도록 한다.
    group_cnt += 1
    return
```
위 코드를 보면 동작 순서는 이렇게 한다.     
1. BFS용 큐를 선언하고, 위치 저장할 스택을 선언한다. 필자는 파이썬 구조 문제점으로 스택 대신 큐를 선언했다.       
2. BFS 큐에 스타트 위치를 푸쉬하고 반복문 아래 하에서 4방향 좌표계를 이용한다.
3. 좌표계에서 이탈하지 않고, 방문하지 않았고, 원래 맵에서 다음 위치가 지날 수 있는 위치이고, 순수한 해당위치 값인지 체크한다.
4. 3번에서 조건들을 다 만족하면 answer에 1씩 증가하고, 다음 위치에 대한 방문처리 하고, 그룹 집합 번호를 매겨주고, 위치를 저장해주고 큐에 푸쉬한다.
5. BFS 큐를 비울 떄까지 반복한다.
6. 저장된 위치값들을 가져오면서 총 길이 값을 담아낸 answer를 저장한다.
7. 저장된 위치 큐를 비우면 그룹 번호를 1씩 증가하고 종료한다.
### 3. setDP 함수를 이용해서 적재시킨다.
```python
visited = [[False for row in range(M)] for col in range(N)]
for col in range(N):
    for row in range(M):
        if not visited[col][row] and arr[col][row] == '0':
            setDP(row, col, visited)
```
### 4. 이젠 벽이 존재하는 위치이면 그 벽의 4방향의 값을 총합해서 10로 나머지 추출한다.
```python
def getCount(x, y):
    answer = 1

    # 0의 그룹 번호가 일치하면 카운트 못 세도록 함.
    group = set()

    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < M and 0 <= Y < N:
            if arr[Y][X] == '0' and group_index_arr[Y][X] not in group:
                answer += group_arr[Y][X]
                group.add(group_index_arr[Y][X])
    return answer % 10
```
```python
for col in range(N):
    tmp = ""
    for row in range(M):
        if arr[col][row] == '1':
            tmp += str(getCount(row, col))
        else:
            tmp += '0'
    result_map.append(tmp)
```
### 5. 문자열로 저장해서 리스트에 담았기 떄문에 바로 간단하게 출력하면 된다.
```python
for v in result_map:
    print(v)
```
