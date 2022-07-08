from collections import defaultdict
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    counts = defaultdict(int)
    for v in a:
        counts[v] += 1
    
    left, right = 0, 0
    for v in counts.values():
        right = max(right, v)
    
    def solve(times):
        rem = n - len(counts.keys())
        rem_t, com_t = 0, 0

        for v in counts.values():
            if v <= times:
                tmp = (times - v)
                com_t += tmp // 2
            else:
                rem_t += v - times
        
        com_t += rem * (times // 2)
        return com_t >= rem_t

    answer = right
    while left <= right:
        mid = (left + right) // 2

        if solve(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(answer)