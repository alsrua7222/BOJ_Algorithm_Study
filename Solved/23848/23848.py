# 풀이 과정
# https://blog.naver.com/alsrua7222/222602301789

import math
N = int(input())
for r in range(2, int(N ** .5) + 1):
    sums = 1 + r
    for n in range(2, int(math.log(N, r)) + 1):
        sums += r ** n
        if N % sums == 0:
            a = N // sums
            print(n + 1)
            for i in range(n + 1):
                print(a * r ** i, end=" ")
            exit(0)
print(-1)
