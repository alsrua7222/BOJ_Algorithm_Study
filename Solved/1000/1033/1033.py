# 풀이 과정
# https://blog.naver.com/alsrua7222/222657685352

import sys
from collections import defaultdict
input = sys.stdin.readline

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
if N == 1:
    print(1)
    exit(0)

Graph = defaultdict(list)
for _ in range(N - 1):
    u, v, q, p = map(int, input().split())
    Graph[u].append([v, p, q])
    Graph[v].append([u, q, p])

for i in Graph.keys():
    Graph[i].sort()

answer = [[0, 0] for _ in range(N)]
answer[0] = [1, 1]

for _ in range(N):
    for u in Graph.keys():
        if answer[u][0] == 0:
            continue
        for v, p, q in Graph[u]:
            if answer[v][0] != 0:
                continue
            child = answer[u][0] * p
            parent = answer[u][1] * q
            g = gcd(child, parent)
            answer[v] = [child // g, parent // g]

LCM = lcm(answer[0][1], answer[1][1])
for i in range(2, N):
    LCM = lcm(LCM, answer[i][1])

for i in range(N):
    print(answer[i][0] * LCM // answer[i][1], end=" ")