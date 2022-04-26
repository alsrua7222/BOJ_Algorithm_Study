# 텀 프로젝트
https://www.acmicpc.net/problem/9466
## 해결 과정
### 0. 골드3 문제가 왜 이리 쉬운가를 생각들었던 것이 착오였다.
### 1. 역시 골드3 답게 수많은 조건들이 존재해 있었다.
### 2. 우선 DFS로 구현하면서 방문 처리를 하게 될텐데 이는 어떻게 구현하냐에 따라 시간초과가 나올 수도 있고, 통과될 수도 있다.
### 3. 방문 처리를 0, 1, 2를 한다. 세부사항은 아래와 같다.
0은 방문하지 않은 순수한 노드 위치.   
1은 방문한 노드 위치.   
2는 방문한 노드에 싸이클 발생한 신호가 있는 노드 위치.    
### 4. 우선 자기 번호와 같은 것이 있는지 검사하고 방문 처리를 2로 처리한다.
### 5. 다시 1부터 시작해서 방문처리가 0으로 되어 있으면 1로 처리하고 DFS를 시행한다.
### 6. DFS의 반환 타입은 boolean 형태이다.
### 7. DFS True이라면 싸이클 발생했다는 의미로 방문 처리를 다시 2로 고친다.
### 8. DFS False이라면 싸이클 발생하지 않았다는 뜻이다.
### 9. 요약하면 아래 소스코드와 같다.
```python
def DFS(arr, start, visited, goal):
    if arr[start] in goal:
        visited[arr[start]] = 2
        visited[start] = 2
        return True
    if visited[start] >= 1:
        return False
    visited[start] = 1
    goal.add(start)
    if DFS(arr, arr[start], visited, goal):
        if visited[start] != 2:
            visited[start] = 2
            return True
        else:
            return False
```
goal은 DFS 방문하면서 지난 노드들의 싸이클 존재가 하는지 검사하기 위한 용도이다.   
list로 적재하면서 검사하기엔 리스크가 크므로, 해쉬테이블로 적재시키면 더 빠르다.     
True로 반환하면서 자기 위치가 2이면 이미 앞에서 찍은 싸이클 신호라는 뜻이다. 그래서 False로 종료시키는 것이다.
### 10. 이렇게 해서 1부터 N까지 반복 수행을 하고 난 후 visited의 1의 개수를 찾는다.
아까 말했듯이 1은 "싸이클 발생하지 않고 방문했다." 라는 뜻이다.  
이것은 소속되지 않은 집합임을 알 수 있다.    
1를 찾으면서 카운트를 센다.
### 11. 카운트 출력한다.
```python
answer = 0
    for v in visited[1:]:
        if v == 1:
            answer += 1
    print(answer)
```
