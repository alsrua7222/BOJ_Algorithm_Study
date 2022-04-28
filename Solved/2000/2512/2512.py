N = int(input())
A = list(map(int, input().split()))
M = int(input())

SUM = 0
MAX = 0
for v in A:
    SUM += v
    MAX = max(MAX, v)

if SUM < M:
    print(MAX)
else:
    A.sort()
    answer = 0
    left, right = 1, MAX
    while left <= right:
        mid = (left + right) // 2
        tmp = 0

        for v in A:
            if mid < v:
                tmp += mid
            else:
                tmp += v
        
        if tmp > M:
            right = mid - 1
        else:
            answer = max(answer, mid)
            left = mid + 1
    print(answer)