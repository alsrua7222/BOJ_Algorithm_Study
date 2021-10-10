from collections import defaultdict, deque
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    Graph = defaultdict(list)
    InDegree = [0] * (N + 1)

    # 위상 정렬을 위해서 차수 개념을 적용. 즉, 차수가 0 아닐 때, 먼저 이수해야하는 것들이 있다.
    for _ in range(K):
        X, Y = map(int, input().split())
        Graph[X].append(Y)
        InDegree[Y] += 1
    W = int(input())
    dp = [0] + [D[i] for i in range(N)]
    Queue = deque()

    # 차수가 0일 때, 푸쉬.
    for i in range(1, N + 1):
        if InDegree[i] == 0:
            Queue.append(i)

    # 비울 때까지 정리.
    while Queue:
        start = Queue.popleft()

        for v in Graph[start]:
            InDegree[v] -= 1
            if InDegree[v] == 0:
                Queue.append(v)
            dp[v] = max(dp[v], dp[start] + D[v - 1])
    print(dp[W])
