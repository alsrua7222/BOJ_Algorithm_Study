from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V = int(input())
Graph = defaultdict(list)
for i in range(V - 1):
    tmp = list(map(int, input().split()))
    Graph[tmp[0]].append([tmp[1], tmp[2]])
    Graph[tmp[1]].append([tmp[0], tmp[2]])

def DFS(start, visited, total):
    visited[start] = True
    global answer
    global MAXSet
    if MAXSet[0] < total:
        MAXSet = [total, start]
    for v, n in Graph[start]:
        if not visited[v]:
            DFS(v, visited, total + n)
MAXSet = [0, 1]
visited = [False] * (V + 1)
DFS(1, visited.copy(), 0)
DFS(MAXSet[1], visited.copy(), 0)
print(MAXSet[0])
