MAX = 1120
prime_check = [True] * (MAX + 1)
primes = []
for i in range(2, MAX + 1):
    if prime_check[i]:
        primes.append(i)
        for j in range(i * 2, MAX + 1, i):
            prime_check[j] = False

dp = [[0 for _ in range(15)] for _ in range(MAX + 1)]
dp[0][0] = 1
for i in range(len(primes)):
    for j in range(MAX, primes[i] - 1, -1):
        for k in range(1, 15):
            dp[j][k] += dp[j - primes[i]][k - 1]

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(dp[n][k])