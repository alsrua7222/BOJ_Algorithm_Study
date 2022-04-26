import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(N + 1)]

def find(x):
    if parents[x] == x:
        return x
    else:
        p = find(parents[x])
        parents[x] = p
        return p

def union(x, y):
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

success = False

for i in range(M):
    n, m = map(int, input().split())
    if success:
        continue
    a = find(n)
    b = find(m)
    if a == b:
        print(i + 1)
        success = True
    union(a, b)

if not success:
    print(0)
