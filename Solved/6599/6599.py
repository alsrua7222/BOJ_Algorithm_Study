# 풀이 과정
# https://blog.naver.com/alsrua7222/222699132301

from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

case = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    arr = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        arr.append((x, y, z))
        arr.append((x, z, y))
        arr.append((y, z, x))

    answer = 0
    Graph = defaultdict(list)
    InDegree = [0] * (N * 3)
    for i in range(N * 3):
        for j in range(N * 3):
            if i == j:
                continue
            if (arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]) or (arr[i][0] < arr[j][1] and arr[i][1] < arr[j][0]):
                Graph[i].append(j)
                InDegree[j] += 1
    
    answer = 0
    Queue = deque()
    dist = [0] * (N * 3)
    for i in range(N * 3):
        if InDegree[i] == 0:
            Queue.append(i)
            dist[i] = arr[i][2]
    
    for i in range(N * 3):
        cur = Queue.popleft()
        for next in Graph[cur]:
            dist[next] = max(dist[next], dist[cur] + arr[next][2])
            InDegree[next] -= 1
            if InDegree[next] == 0:
                Queue.append(next)

    print(f"Case {case}: maximum height = {max(dist)}")
    case += 1