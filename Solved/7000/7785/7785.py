import sys
input = sys.stdin.readline
N = int(input())
set1 = set()
for _ in range(N):
	name, state = input().split()
	if state[0] == 'e':
		if name not in set1:
			set1.add(name)
	else:
		if name in set1:
			set1.remove(name)
for v in sorted(set1, reverse=True):
	print(v)
