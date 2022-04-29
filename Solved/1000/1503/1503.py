N, M = map(int, input().split())
if M != 0:
    A = set(list(map(int, input().split())))
else:
    A = set()
answer = float('inf')
for i in range(1, 1002):
    if i in A:
        continue
    for j in range(i, 1002):
        if j in A:
            continue
        for k in range(j, 1002):
            if k in A:
                continue
            answer = min(answer, abs(N - i * j * k))
            if N + 1 < i * j * k:
                break
print(answer)