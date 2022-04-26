N, M = map(int, input().split())
trues = list(map(int, input().split()))[1:]
partys = []
parents = [i for i in range(N + 1)]
for _ in range(M):
    partys.append(list(map(int, input().split()))[1:])


def find(n):
    if parents[n] == n:
        return n
    else:
        n = find(parents[n])
        return n

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return

for v in partys:
    for i in range(len(v) - 1):
        union(v[i], v[i + 1])
answer = 0
for v in partys:
    check = False
    for v2 in v:
        if check:
            break
        for i in range(len(trues)):
            if find(trues[i]) == find(v2):
                check = True
                break
    if check:
        answer += 1
print(M - answer)
