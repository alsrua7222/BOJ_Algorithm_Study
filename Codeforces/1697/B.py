import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
dp = []
dp.append(a[0])
for v in a[1:]:
    dp.append(dp[-1] + v)

for _ in range(q):
    x, y = map(int, input().split())
    if x == y:
        print(dp[x - 1])
    else:
        print(dp[x - 1] - dp[x - y - 1])