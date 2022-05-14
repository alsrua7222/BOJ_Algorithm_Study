import math, itertools
arr = list(map(int, input().split()))

answer = float('inf')
for v1, v2, v3 in itertools.combinations(arr, 3):
    answer = min(answer, math.lcm(v1, v2, v3))
print(answer)