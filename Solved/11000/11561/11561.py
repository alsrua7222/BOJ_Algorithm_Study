import sys
input = sys.stdin.readline

collect = []
for _ in range(int(input())):
    n = int(input())
    goal = n

    answer = 1
    left, right = 1, n
    
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 == goal:
            answer = mid
            break
        elif mid * (mid + 1) // 2 < goal:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    collect.append(answer)
print(*collect, sep="\n")