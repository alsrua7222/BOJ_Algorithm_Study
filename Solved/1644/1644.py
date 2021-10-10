def IsPrime(N):
    for i in range(2, int(N ** .5) + 1):
        if N % i == 0:
            return False
    return True

N = int(input())
cnt = 0
if 2 <= N <= 3:
    print(1)
    exit(0)
elif N == 1:
    print(0)
    exit(0)
else:
    if IsPrime(N):
        cnt += 1

# 크기 2로 나눠보면 56%에서 틀림.
# 다시 루트2로 나눠보면 91%에서 틀림.
# 크기를 최대한 줄여서 빠르게 처리하고 싶었는데 그게 안되나봐.
MAX = int((N + 1))
dp = [True] * MAX
primes = []
for i in range(2, MAX):
    if dp[i]:
        primes.append(i)
        for j in range(i, MAX, i):
            dp[j] = False

x = 0
y = 0
total = 0
while y < len(primes):
    if total < N:
        total += primes[y]
        y += 1
    else:
        if total == N:
            cnt += 1
        total -= primes[x]
        x += 1
print(cnt)
