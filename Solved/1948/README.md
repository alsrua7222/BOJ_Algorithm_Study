# 임계경로
https://www.acmicpc.net/problem/1948
## 해결 과정
### 0. 위상 정렬으로 풀면 된다. 
문제를 이해가 안되서 찾아오는 분들 있을텐데, 문제를 꼬와서 제출했기 때문에 해석이 어려운건 맞다.     
핵심 키워드를 보면 위상 정렬로 풀어야 한다는 것을 알 수 있을 것이다.        
출발 도시는 무조건 들어오는 도로가 0개이고, 도착 도시는 나가는 도로가 0개이다.      
그리고 입력단에서 출발 도시와 도착 도시는 무조건 주어지게 되어 있다.
즉, 차수가 0인 인덱스를 한방에 찾게 도와주는 것이다.     
### 1. 위성정렬로 풀면 답이 나오지만, 문제는 도로의 개수를 카운팅 해서 출력해야 한다. 이 조건은 아래와 같다.
어떤 사람이 1분도 쉬지 않고 계속 달리는 도로이어야 한다.       
그 특정된 도로를 카운팅 집계로 쌓는다.      
즉, 가장 오래 걸린 경로를 찾아서 그 경로의 도로 개수를 찾으라는 뜻이다.       
난 이 말을 이해하기 까지 오래 걸렸다.           
본 문제의 입력 데이터들에 따르면      
1 -> 2 -> 6 -> 7인 경로는 12가 나오고, 1 -> 4 -> 6 -> 7인 경로도 12로 나온다.       
이 때 도로의 개수를 구할 땐,       
1 -> 2, 2 -> 6, 6 -> 7 이고       
1 -> 4, 4 -> 6, 6 -> 7 이다.      
겹친 도로를 하나로 줄이고 보면.      
1 -> 2, 1 -> 4, 2 -> 6, 4 -> 6, 6 -> 7가 되고,     
총 5개가 있다고 말할 수 있다.      
### 2. 도로의 개수를 구하는 방법이 다양했다. 사용한 방법과 결과는 아래와 같다.
1번째는 거꾸로된 그래프로 순회하면서 현재 가중치 값을 빼면서 도로 카운팅 해준다.     
그러면 마지막에 가장 오래 걸린 시간이랑 비교해서 같으면 도로 카운팅을 set에 넣는다.       
다르면 안 넣도록 한다.       
당연히 *시간초과* 터졌다. 이유는 모든 경우의 수를 접근했기 때문이다.        

2번째는 path 경로를 추가해서 다음 상태 값이 현재 상태 값보다 작다면 초기화 한 후,      
path 경로를 현재 상태의 경로들에 다음 상태 번호를 추가해서 적재시킨다.      
말로는 이해가 안될 것이다. 아래와 보면 된다.
```python
import sys, heapq
input = sys.stdin.readline
from collections import defaultdict

# https://www.acmicpc.net/problem/1948

N = int(input())

# 위상 정렬
Graph = defaultdict(list)
InDegree = [0] * (N + 1)
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    Graph[A].append([B, C])
    InDegree[B] += 1

# 최단 거리 기법을 적용해서 그리디하게 가장 큰 값을 나중에 적재시키기.
start, end = map(int, input().split())
Queue = []
heapq.heappush(Queue, [0, start, [start]])

arr = [0] * (N + 1)
# 역추적 사용 실패로 DP 기법을 사용하기 위해 path 배열 추가.
arr_path = [list() for i in range(N + 1)]
arr_path[start] = [[start]]

while Queue:
    w, node, path = heapq.heappop(Queue)

    for next, W in Graph[node]:
        InDegree[next] -= 1
        total = max(arr[next], w + W)
        if InDegree[next] == 0:
            heapq.heappush(Queue, [total, next, path + [next]])

        if arr[next] < w + W:
            # 다음 상태 값이 현재 상태의 길이의 합보다 작다면
            if arr_path[next]:
                # 다음 상태의 경로가 존재한다면
                # 이들은 현재 상태의 길이 합보다 작다는 신호이므로 초기화한다.
                arr_path[next] = []
                # 초기화 한 후, 현재 상태의 경로들을 다음 상태의 경로에 추가한다.
                for v in arr_path[node]:
                    arr_path[next].append(v + [next])
            else:
                # 다음 상태의 경로가 없다면, 갖고 있는 큐 path를 가져와서 초기화한다.
                arr_path[next] = [path + [next]]
        elif arr[next] == w + W:
            # 다음 상태 값이 가중치의 길이와 같다면
            # 현재 상태의 경로들을 가져와서 적재시킨다.
            for v in arr_path[node]:
                arr_path[next].append(v + [next])

        # 경로 작업 끝나면 상태 값 저장한다.
        arr[next] = total

print(arr[end])

# 역추적 사용 못하는 이유는 모든 방문을 하기 때문이다.
# path 배열을 추가해서 DP원리를 적용해서 시간 초과를 줄인다.
set1 = set()
for v in arr_path[end]:
    for i in range(1, len(v)):
        set1.add((v[i - 1], v[i]))
print(len(set1))
```
DP 원리를 이용해서 해봤으나, 시간 초과 대신 *메모리 초과*가 떴다.        

3번째는 아까 1번째와 비슷하게 동작하는 대신, 미리 받아놓은 arr 상태 값들을 비교해 가면서 같으면 추가하고, 아니라면 아무 동작을 하지 않도록 한다.      
거꾸로된 그래프를 당연히 이용해야 한다.      
그랬더니 제출 성공하였다.      
1번째 방법이 정해였는데 내가 크게 너무 돈 것 같았다.     
코드는 아래와 같다.
```python
import sys
input = sys.stdin.readline
from collections import defaultdict, deque
N = int(input())
Graph = defaultdict(list)
Reverse_Graph = defaultdict(list)
InDegree = [0] * (N + 1)
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    Graph[A].append([B, C])
    Reverse_Graph[B].append([A, C])
    # Graph[B].append([A, C])
    InDegree[B] += 1

start, end = map(int, input().split())
Queue = deque()
Queue.append([start, 0])

arr = [0] * (N + 1)
while Queue:
    node, w = Queue.pop()

    for next, W in Graph[node]:
        InDegree[next] -= 1
        total = max(arr[next], w + W)
        if InDegree[next] == 0:
            Queue.append([next, total])
        arr[next] = total

print(arr[end])

# 역추적
Queue.append(end)
visited = [False for i in range(N + 1)]
answer = 0
while Queue:
    node = Queue.popleft()
    for next, w in Reverse_Graph[node]:
        if arr[node] - w == arr[next]:
            answer += 1
            if not visited[next]:
                visited[next] = True
                Queue.append(next)
print(answer)
```
### 3. 역추적 방법이 정해였음을 깨달았고, 이를 출력했다.
