import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0
for v in A:
    v -= B
    if v <= 0:
        answer += 1
    else:
        answer += 1 + (math.ceil(v / C))
print(answer)