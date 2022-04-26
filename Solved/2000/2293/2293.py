N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
dp = [0] * (K + 1)
# 0원 만드는 경우의 수는 딱 1가지.
dp[0] = 1

# n원 만드는 경우의 수는 동전의 금액이랑 빼서 계산하면 된다.
# 바텀업 방식으로 올라가야 한다.
for i in range(N):
    tmp = arr[i]
    j = 0
    while j + tmp <= K:
        dp[j + tmp] += dp[j]
        j += 1
print(dp[-1])
