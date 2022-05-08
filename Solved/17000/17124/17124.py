import bisect
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    answer = 0
    for i in range(n):
        index = bisect.bisect_left(b, a[i])
        if index == 0:
            answer += b[index]
        elif index == m:
            answer += b[m - 1]
        else:
            left = abs(b[index - 1] - a[i])
            right = abs(b[index] - a[i])
            if left <= right:
                answer += b[index - 1]
            else:
                answer += b[index]
    print(answer)