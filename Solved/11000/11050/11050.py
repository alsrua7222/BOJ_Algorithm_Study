N, K = map(int, input().split())
answer = 1
cnt = 0
while cnt < K:
    answer *= (N - cnt)
    cnt += 1
cnt = 1
while cnt <= K:
    answer //= cnt
    cnt += 1
print(answer)
