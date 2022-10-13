import sys
from collections import deque
input = sys.stdin.readline
"""
TLE 떠서 C++로 바꿈.
"""
def solve(n, arr):
    idx = n - 1
    sort = deque(sorted(list([v, v] for v in arr)))
    bit = 0
    answer = []
    for i in range(n):
        answer.append(sort[-1][1])
        flag = False
        for j in range(30):
            if (bit >> j) & 1 == 0 and (sort[-1][1] >> j) & 1 == 1:
                for k in range(len(sort)):
                    sort[k][0] &= (2147483647 ^ (1 << j))
                flag = True
        bit = bit | sort[-1][1]
        sort.pop()
        if flag:
            sort = deque(sorted(sort))
    return answer

for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(*solve(n, a))
    