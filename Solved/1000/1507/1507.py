# 풀이 과정
# https://blog.naver.com/alsrua7222/222606263989

import sys
sys = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
	arr.append(list(map(int, input().split())))

dp = [[1 for _ in range(N)] for _ in range(N)]

for k in range(N):
	for i in range(N):
		for j in range(N):
			if k == i or k == j or i == j:
				continue
			if arr[i][j] > arr[i][k] + arr[k][j]:
				print(-1)
				exit(0)
			elif arr[i][j] == arr[i][k] + arr[k][j]:
				dp[i][j] = 0

answer = 0
for i in range(N):
	for j in range(i + 1, N):
		if dp[i][j]:
			answer += arr[i][j]
print(answer)
