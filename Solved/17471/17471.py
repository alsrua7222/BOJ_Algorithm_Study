from collections import defaultdict, deque
from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
people = list(map(int, input().split()))
Graph = defaultdict(list)
for i in range(1, N + 1):
    tmp = list(map(int, input().split()))[1:]
    for j in range(len(tmp)):
        Graph[i].append(tmp[j])
        Graph[tmp[j]].append(i)


def BFS(arr):
    Queue = deque()
    Queue.append(arr[0])
    visited = [True] * (N + 1)
    for v in arr:
        visited[v] = False
    visited[arr[0]] = True

    while Queue:
        num = Queue.popleft()
        for v in Graph[num]:
            if not visited[v]:
                visited[v] = True
                Queue.append(v)
    if sum(visited) == N + 1:
        return True
    else:
        return False


peoples = set((i for i in range(1, N + 1)))
answer = 987654321
# 모든 경우의 수를 따져봐야 하니 조합 iterator를 사용한다.
for i in range(1, N // 2 + 1):
    for team1 in combinations(range(1, N + 1), i):
        team2 = tuple(peoples.copy() - set(team1))
        if BFS(team1) and BFS(team2):
            sum1 = 0
            for v in team1:
                sum1 += people[v - 1]
            sum2 = 0
            for v in team2:
                sum2 += people[v - 1]
            answer = min(abs(sum1 - sum2), answer)
print(answer if answer != 987654321 else -1)
