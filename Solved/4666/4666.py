# 풀이 과정
# https://blog.naver.com/alsrua7222/222686550759

from collections import deque, defaultdict
from math import *
import sys
input = sys.stdin.readline
Graph = defaultdict(list)

def BFS(start, end):
    queue = deque([[start, 1, 1]])
    visited = set()
    visited.add(start)
    while queue:
        cur, child, parent = queue.popleft()
        
        for next, c, p in Graph[cur]:
            if next == end:
                return [child * p, parent * c]
            if next not in visited:
                queue.append([next, child * p, parent * c])
                visited.add(next)
    return -1

while True:
    query = input().rstrip()
    if query[0] == '.':
        break
    elif query[0] == '!':
        query = query.split()
        u = query[2]
        a = int(query[1])
        v = query[5]
        b = int(query[4])
        Graph[u].append((v, a, b))
        Graph[v].append((u, b, a))
    else:
        query = query.split()
        tmp = BFS(query[1], query[3])
        if tmp == -1:
            print(f"? {query[1]} = ? {query[3]}")
        else:
            tmp2 = gcd(tmp[0], tmp[1])
            print(f"{tmp[1] // tmp2} {query[1]} = {tmp[0] // tmp2} {query[3]}")
