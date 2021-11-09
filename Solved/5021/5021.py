from collections import defaultdict
Graph = defaultdict(list)
Blood = defaultdict(float)
InDegree = defaultdict(int)
N, M = map(int, input().split())
start = input()
Blood[start] = 1.0
for _ in range(N):
    child, parent1, parent2 = input().split()
    Graph[child].append(parent1)
    Graph[child].append(parent2)

def backTracking(name):
    if name not in Graph:
        return Blood[name]
    p1, p2 = Graph[name]
    Blood[name] = (backTracking(p1) + backTracking(p2)) / 2
    return Blood[name]

answer = [0, ""]
for _ in range(M):
    name = input()
    tmp = backTracking(name)
    if tmp > answer[0]:
        answer = [tmp, name]
print(answer[1])

