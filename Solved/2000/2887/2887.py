import sys
input = sys.stdin.readline
N = int(input())
parents = [0] + [i for i in range(1, N + 1)]

# arr로도 메모리초과가 난다면? 그냥 정렬해서 union-find 해야할 것 같다.
X = []
Y = []
Z = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    X.append([tmp[0], _])
    Y.append([tmp[1], _])
    Z.append([tmp[2], _])

X.sort()
Y.sort()
Z.sort()
def find(x):
    if parents[x] == x:
        return x
    else:
        p = find(parents[x])
        parents[x] = p
        return p
def union(x, y):
    parents[y] = x
    return

arr2 = []
for i in range(1, N):
    arr2.append([abs(X[i][0] - X[i - 1][0]), X[i][1], X[i - 1][1]])
for i in range(1, N):
    arr2.append([abs(Y[i][0] - Y[i - 1][0]), Y[i][1], Y[i - 1][1]])
for i in range(1, N):
    arr2.append([abs(Z[i][0] - Z[i - 1][0]), Z[i][1], Z[i - 1][1]])

arr2.sort()

answer = 0
for v in arr2:
    ar = find(v[1])
    br = find(v[2])
    if ar != br:
        union(ar, br)
        answer += v[0]
print(answer)
