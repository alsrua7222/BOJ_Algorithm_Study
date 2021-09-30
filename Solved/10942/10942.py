import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[False for _ in range(2001)] for _ in range(2001)]

for index in range(1, N + 1):
	dp[index][index] = True
	if index != 1 and arr[index - 2] == arr[index - 1]:
		dp[index - 1][index] = True

for i in range(2, N + 1):
	j = 1
	while i + j <= N:
		if arr[j - 1] == arr[i + j - 1] and dp[j + 1][i + j - 1]:
			dp[j][i + j] = True
		j += 1

for _ in range(int(input())):
	X, Y = map(int, input().split())
	print(1 if dp[X][Y] else 0)
