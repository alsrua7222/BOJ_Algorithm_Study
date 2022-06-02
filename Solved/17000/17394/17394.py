from collections import deque

MAX = 1000001
primes = [True] * MAX
primes[0] = primes[1] = False
for i in range(2, MAX):
    if primes[i]:
        for j in range(i*i, MAX, i):
            primes[j] = False

def IsSubPrime(_from, _to):
    for i in range(_from, _to + 1):
        if primes[i]:
            return True
    return False

def BFS(N, A, B):
    if not IsSubPrime(A, B):
        return -1
    
    visited = [False] * MAX
    Queue = deque([[N, 0]])
    visited[N] = True
    while Queue:
        cur, cnt = Queue.popleft()

        if cur == 0:
            continue

        if A <= cur <= B and primes[cur]:
            return cnt

        if cur // 3 > 0 and not visited[cur // 3]:
            Queue.append([cur // 3, cnt + 1])
            visited[cur // 3] = True        

        if cur // 2 > 0 and not visited[cur // 2]:
            Queue.append([cur // 2, cnt + 1])
            visited[cur // 2] = True
        
        if cur - 1 > 0 and not visited[cur - 1]:
            Queue.append([cur - 1, cnt + 1])
            visited[cur - 1] = True
        
        if cur + 1 < MAX and not visited[cur + 1]:
            Queue.append([cur + 1, cnt + 1])
            visited[cur + 1] = True
    return -1

for _ in range(int(input())):
    N, A, B = map(int, input().split())

    print(BFS(N, A, B))