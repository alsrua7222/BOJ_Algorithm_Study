import sys
sys.setrecursionlimit(10**6)
N = int(input())
visited = [False] * (N + 1)
def permutation(cur, collect):
    if cur == N:
        print(' '.join(map(str, collect)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            permutation(cur + 1, collect + [i])
            visited[i] = False
permutation(0, [])