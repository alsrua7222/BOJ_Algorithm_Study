# 연결 요소의 개수
https://www.acmicpc.net/problem/11724
## 해결 과정
### 0. 연결된 그래프끼리 체크해서 몇 개 있는지 하는 문제다.
### 1. 양방향 그래프이므로 둘다 노드 적재시킨다.
Graph[u] <- v   
Graph[v] <- u   
### 2. 1번째부터 N번째까지 선형 반복으로 돌려서 시행한다.
### 3. 시행할 때 카운트를 증가시키고 방문 처리를 해놓으면 된다.
연결된 그래프끼리 방문처리가 되고, 사후처리가 잘 된다.   
### 4. 그렇게 해서 누적합된 카운트를 출력.
