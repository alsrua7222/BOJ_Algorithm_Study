# 작업
https://www.acmicpc.net/problem/2056
## 해결 과정
### 0. 위상정렬으로 풀어야 한다.
### 1. i번째 작업에 선행 조건 쿼리가 주어지는대로 그래프 연결해준다. 
이는 복잡하게 생각할 필요가 없다.     
선행조건의 개수는 곧 차수의 개수임을 나타낸다.      
그리고 선행조건들과 i번쨰 작업을 서로 연결되게 만든다.     
### 2. 차수가 0인 노드를 찾아내고 answer[i]에 걸린 시간을 넣고 최소힙에 적재시킨다.
```python
# 본 문제에서는 항상 1번 작업이 시작점이다. 그렇지만, 하나만 있는게 아니라 둘 이상 있을 수도 있으므로 반드시 검사해서 큐에 적재시킨다.
HQ = []
answer = [987654321] * (N + 1)
for i in range(1, N + 1):
    if InDegree[i] == 0:
        heapq.heappush(HQ, [Times[i], i])
        answer[i] = Times[i]
```
### 3. 최소힙으로 원소를 빼면서 잡다한 최소 시간들을 전부 싹다 정리한 후, 마지막에 남은 시간으로 answer에 저장해준다.
```python
while HQ:
    times, cur = heapq.heappop(HQ)

    for v in Graph[cur]:
        InDegree[v] -= 1
        if InDegree[v] == 0:
            heapq.heappush(HQ, [times + Times[v], v])
        answer[v] = times + Times[v]
```
### 4. answer 중에서 가장 큰 값을 출력한다.
```python
print(max(answer[1:]))
```
