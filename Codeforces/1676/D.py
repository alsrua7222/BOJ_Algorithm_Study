dp = [0, 0, 2]
while dp[-1] <= 10**9:
    N = len(dp) // 3
    if len(dp) % 3 == 0:
        dp.append(6 * N ** 2)
    elif len(dp) % 3 == 1:
        dp.append(6 * N ** 2 + 4 * N)
    else:
        dp.append(6 * N ** 2 + 8 * N + 2)

import bisect, sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    print(bisect.bisect_left(dp, n))