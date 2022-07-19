N, K = map(int, input().split())
a = list(map(int, input().split()))

MOD = int(1e9 + 7)
A, B = 1, 1
for i in range(1, N + 1): # n!
    A = (A * i) % MOD
for i in range(1, K + 1): # k!
    B = (B * i) % MOD
for i in range(1, N - K + 1): # k! (n - k)!
    B = (B * i) % MOD

base = 1
ex = MOD - 2
while ex > 0:
    if ex & 1 == 1:
        base = (base * B) % MOD
    B = (B ** 2) % MOD
    ex //= 2

nCk = (A * base) % MOD
print((nCk * (2 ** (K - 1))) % MOD)