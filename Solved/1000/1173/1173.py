N, m, M, T, R = map(int, input().split())
if m + T > M:
    print(-1)
    exit(0)

answer = 0
tmp = m
cnt = 0
while cnt < N:
    answer +=1
    if tmp + T <= M:
        tmp += T
        cnt += 1
    else:
        tmp -= R
        if tmp < m:
            tmp = m
print(answer)