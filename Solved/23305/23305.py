import sys
input = sys.stdin.readline
N = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))
x, y = 0, 0
answer = 0
while x < N and y < N:
	if arr1[x] > arr2[y]:
		y += 1
	elif arr1[x] < arr2[y]:
		x += 1
	else:
		answer += 1
		x += 1
		y += 1
print(N - answer)
