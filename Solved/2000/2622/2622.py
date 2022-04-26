import math
N = int(input())
first = int(math.ceil(N / 3))
second = N // 2 - (0 if N & 1 else 1)

answer = 0
for C in range(first, second + 1):
    answer += (C - (N - C) // 2)
    if not (N - C) & 1:
        answer += 1
print(answer)
