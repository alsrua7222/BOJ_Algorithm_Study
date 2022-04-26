# 별자리 만들기
https://www.acmicpc.net/problem/4386
## 해결 과정
### 0. MST(Minimum Spanning Tree)를 써야 풀리는 문제이다.
### 1. 크루스칼 알고리즘을 사용해서 모든 간선의 가중치를 최소힙에 적재 시킨다.
```
def getDistance(a, b):
    tmp1 = (a[0] - b[0]) ** 2
    tmp2 = (a[1] - b[1]) ** 2
    return (tmp1 + tmp2) ** .5
```
간선의 가중치 값을 반환해서 i번째 j번째 원소다. 라는 정보로 추가해서 적재 시킨다.
```
for i in range(N - 1):
    for j in range(i + 1, N):
        heapq.heappush(HQ, [getDistance(arr[i], arr[j]), i, j])
```
### 2. union-find 기법으로 간소화시킨 i번째 j번째를 이용해서 빠르게 푼다.
```
parent = [-1] * (N + 1)
def find(x):
    if parent[x] < 0:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p
def union(x, y):
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
```
### 3. cnt를 0으로 선언한 다음에 MST 조건에 따라 연결된 간선 N - 1개로 될 때 까지 아래와 같이 반복한다.
최소힙을 빼낸 후 dist과 i번째와 j번째를 받는다.    
find함수로 i번째가 부모인지 자식인지 체크한다. 부모면 i번쨰이고, 자식이면 부모를 가리키는 인덱스를 반환한다.    
j번쨰도 적용한다.    
i랑 j가 서로 같은지 비교한다. 다르면 좋다.    
다르면 union 함수를 사용해서 하나 부모를 제거한 후 다른 부모에 종속시키고 answer에 dist를 적재시키고 연결됐다는 뜻으로 간선 카운트 하나 증가 시킨다.    
여기서 i번째가 j번째로 종속 시킨다는 듯이다.    
반대도 j번째가 i번째로 종속 시킨다는 것도 있다.    
```
cnt = 0
answer = 0
while cnt != N - 1:
    dist, a, b = heapq.heappop(HQ)
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        answer += dist
        cnt += 1
```
### 4. MST 간선 개수 조건을 만족하면 종료하고 소수점 2번째 자리까지 표현하고 끝낸다.
