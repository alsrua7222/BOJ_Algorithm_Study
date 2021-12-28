# 풀이 과정
# https://blog.naver.com/alsrua7222/222607104705
import sys
from heapq import *
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = []
G = defaultdict(list)
GR = defaultdict(list)
InDegree = [0] * N # 진입 차수
OutDegree = [0] * N # 진출 차수
for i in range(N):
    arr.append(list(map(int, list(input().rstrip()))))
    for j in range(N):
        if arr[-1][j] == 1 and i == j:
            print(-1)
            exit(0)
        if arr[-1][j] == 1:
            # G[i].append(j)
            GR[j].append(i)
            # InDegree[j] += 1
            OutDegree[i] += 1

# 위상 정렬 시작.
Queue = []
for i in range(N):
    if OutDegree[i] == 0:
        heappush(Queue, -i)

answer = [0] * N
rank = N
try:
    for i in range(N):
        cur = -heappop(Queue)
        answer[cur] = rank
        rank -= 1
        for v in GR[cur]:
            OutDegree[v] -= 1
            OutDegree[cur] -= 1
            if OutDegree[v] == 0:
                heappush(Queue, -v)
    print(*answer)
except Exception as e:
    print(-1)
    exit(0)
