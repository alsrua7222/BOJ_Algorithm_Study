# 풀이 과정
# https://blog.naver.com/alsrua7222/222617348483

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = defaultdict(list)
C = 0
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])
    C = max(C, w)

s, e = map(int, input().split())

def BFS(start, end, limit):
    Queue = deque()
    Queue.append(start)
    visited = [False] * (N + 1)
    visited[start] = True
    while Queue:
        cur = Queue.popleft()

        for next, weight in G[cur]:
            if visited[next] or weight <= limit:
                continue
            visited[next] = True
            if next == end:
                return True
            Queue.append(next)
    return False

left = 1
right = C
while left < right:
    mid = (left + right) // 2
    if BFS(s, e, mid):
        left = mid + 1
    else:
        right = mid
print(left)
