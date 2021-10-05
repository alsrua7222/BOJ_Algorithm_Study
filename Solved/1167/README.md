# 트리의 지름
https://www.acmicpc.net/problem/1167
## 해결 과정
### 0. DFS로 푼다.
BFS로 해결하려다 정점 V의 개수가 100,000임을 확인하고 취소함.    
### 1. 어느 노드부터 시작해야 최대거리를 구할 수 있을까를 생각해봐야 함.
### 2. 우선 1번째 노드부터 시작해서 최장 거리를 기록한 노드를 갱신한다.
### 3. 최장 거리를 기록한 노드부터 한번 더 DFS 해본다.
### 4. 그러면 끝이다.