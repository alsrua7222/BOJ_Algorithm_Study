import math, sys
input = sys.stdin.readline
for _ in range(int(input())):
	x, y = map(int, input().split())
	# 거리에 따라 똑같은 패턴을 발견함.
	r = math.floor((y - x) ** .5 + .5)
	if y - x <= r ** 2:
		print(r * 2 - 1)
	else:
		print(r * 2)
