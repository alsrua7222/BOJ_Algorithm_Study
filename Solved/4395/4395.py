# 풀이 과정
# https://blog.naver.com/alsrua7222/222630179772

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print(0)
    else:
        r = int((y - x) ** .5 + .5)
        if y - x <= r ** 2:
            print(r * 2 - 1)
        else:
            print(r * 2)