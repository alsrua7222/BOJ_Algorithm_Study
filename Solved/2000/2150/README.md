# Strongly connected component
https://www.acmicpc.net/problem/2150
## 해결 과정
### 0. DFS로 탐색하면서 더 이상 탐색할 수 없는 경우, 종료하면서 스택에 현재 상태 정보를 담는다.
### 1. 그렇게 해서 1번부터만 탐색할게 아니라 모든 노드부터 꼼꼼히 탐색해야 한다.
### 2. 스택에 다 쌓은 후, 원소 하나씩 빼면서 방문 처리가 안됬으면 거꾸로된 그래프를 DFS로 방문한다.
### 3. 탐색하면서 방문 처리를 한 후, 더 이상 탐색하지 않는다면, 현재 상태를 기록하면서 종료한다.
### 4. 기록한 배열을 오름차순 한 후 정답 배열에 추가하고, 스택 원소를 빼서 전과 같은 동작을 수행한다.
### 5. 스택 다 비우면 정답 배열을 1번째 원소 기준으로 오름차순 하고 정답 출력한다.
### 6. 나중에 코사라주 알고리즘이랑 유사하게 짰다는 사실을 알았다.
