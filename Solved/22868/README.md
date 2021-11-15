# 산책(small)
https://www.acmicpc.net/problem/22870
## 해결 과정
### 0. 최단거리 알고리즘으로 풀면 쉽다.
### 1. 먼저 그래프 노드를 생성한 다음, 사전 순 조건에 맞게 작업해놓은 그래프를 정렬한다.
### 2. 우선 end에서 start로 가는 최단 거리를 구한다. 그래야 start에서 end까지 가는 경로 중에서 사전 순으로 앞서는 경로를 고를 수 있으니까.
### 3. 구한 최단거리로 최적 경로를 찾으면서 방문 처리한다.
```python
dist = dijkstra(end)

cur = start
length = 0
while end != cur:
    for next in Graph[cur]:
        if length + 1 + dist[next] == dist[start]:
            visited[next] = True
            length += 1
            cur = next
            break

visited[end] = False
```
### 4. 방문 처리하고 최단 거리 한번 더 구한다.
```python
print(dist[start] + dijkstra(start)[end])
```