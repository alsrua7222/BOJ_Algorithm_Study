# 풀이 과정
# https://blog.naver.com/alsrua7222/222705598381

X, Y = map(int, input().split())
Z = int(Y * 100 / X)

if Z >= 99:
    print(-1)
else:
    left, right = 0, 1000000000
    answer = float('inf')
    while left <= right:
        mid = (left + right) // 2
        if Z != int((Y + mid) * 100 / (X + mid)):
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    print(answer)