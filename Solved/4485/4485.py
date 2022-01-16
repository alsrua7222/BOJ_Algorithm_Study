# 풀이 과정
# https://blog.naver.com/alsrua7222/222623130201
from collections import defaultdict
import heapq

N, M, X = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    u, v, w, c = map(int, input().split())
    G[u].append([v, w, c])
    G[v].append([u, w, c])

def dijkstra():
    HQ = []
    nodes = [float('inf')] * (N + 1)
    heapq.heappush(HQ, [0, 1, [0, 0, 0]])

    nodes[1] = 0
    answer = []
    while HQ:
        w, cur, collect = heapq.heappop(HQ)
        # if nodes[cur] < w:
        #     continue
        for next, weight, color in G[cur]:
            if nodes[next] > w + weight:
                nodes[next] = w + weight
                tmp = collect.copy()
                tmp[color] += 1
                if next == N:
                    answer.clear()
                    answer.append([w + weight, tmp])
                else:
                    heapq.heappush(HQ, [w + weight, next, tmp])
            elif next == N and nodes[next] == w + weight:
                tmp = collect.copy()
                tmp[color] += 1
                answer.append([w + weight, tmp])
    return answer

print(dijkstra())