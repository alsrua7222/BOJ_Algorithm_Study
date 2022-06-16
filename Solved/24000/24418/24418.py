N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
cache = [[0 for _ in range(N + 1)] for _ in range(2 * N + 1)]
def solve(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if cache[n][r] != 0:
        return cache[n][r]
    cache[n][r] = solve(n - 1, r - 1) + solve(n - 1, r)
    return cache[n][r]
print(solve(2 * N, N), N * N)