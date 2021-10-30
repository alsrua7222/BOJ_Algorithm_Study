# 게리맨더링
https://www.acmicpc.net/problem/17471
## 해결 과정
### 0. 패턴을 찾아서 해결하는 식이 아닌 전체 탐색을 해서 그 중에 최솟값을 출력하는 것이다.
### 1. 그러면 경우의 수가 N개에 따라서 틀리다. 아래 조건와 같다.
N = 6개 라면,
[1], [2, 3, 4, 5, 6]        
[2], [1, 3, 4, 5, 6]        
...     
[6], [1, 2, 3, 4, 5]        
[1, 2], [3, 4, 5, 6]        
...     
[2, 3, 4, 5, 6], [1]        
대충 이렇게 계산할 수 있다.
단, 이미 계산 했던 쪽을 다시 할 필요가 없으니     
반을 접어서 계산하듯이 2로 나눠주고 경우의 수를 따지면 되겠다.        
```python
for i in range(1, N // 2 + 1):
    for team1 in combinations(range(1, N + 1), i):
        # 생략
```
combinations의 iterator를 이용해서 빠르게 푼다.        
### 2. BFS 구현을 해서 각 팀의 속한 구 번호를 방문 처리한다.
```python
def BFS(arr):
    Queue = deque()
    Queue.append(arr[0])
    visited = [True] * (N + 1)
    for v in arr:
        visited[v] = False
    visited[arr[0]] = True

    while Queue:
        num = Queue.popleft()
        for v in Graph[num]:
            if not visited[v]:
                visited[v] = True
                Queue.append(v)
```
### 3. 방문처리하면서 탐색하다가 종료되고 모두 방문했다면 True 반환, 아니라면 False 반환해준다.
```python
def BFS(arr):
    # 생략
    if sum(visited) == N + 1:
        return True
    else:
        return False
```
### 4. 각 팀의 BFS 탐색이 모두 참이라면 조건 맞췄다는 뜻으로, 최솟값 설정한다.
```python
peoples = set((i for i in range(1, N + 1)))
answer = 987654321
# 모든 경우의 수를 따져봐야 하니 조합 iterator를 사용한다.
for i in range(1, N // 2 + 1):
    for team1 in combinations(range(1, N + 1), i):
        team2 = tuple(peoples.copy() - set(team1))
        if BFS(team1) and BFS(team2):
            sum1 = 0
            for v in team1:
                sum1 += people[v - 1]
            sum2 = 0
            for v in team2:
                sum2 += people[v - 1]
            answer = min(abs(sum1 - sum2), answer)
print(answer if answer != 987654321 else -1)
```
### 5. 출력한다.
