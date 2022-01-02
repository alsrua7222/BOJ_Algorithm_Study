# 풀이 과정
# https://blog.naver.com/alsrua7222/222611162524
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
G = defaultdict(list)
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited_count = [0] * (V + 1)
global_count = 1

def DFS(cur, pre):
    global global_count, answer
    visited_count[cur] = ret = global_count
    global_count += 1

    for next in G[cur]:
        if next == pre:
            continue

        if visited_count[next]:
            ret = min(ret, visited_count[next])
        else:
            tmp = DFS(next, cur)
            if ret > tmp:
                ret = tmp
            if tmp > visited_count[cur]:
                answer.append([cur, next])

    return ret


answer = []
DFS(1, 0)

print(len(answer))
for v in sorted(list(sorted(v) for v in answer)):
    print(*v)
