import sys
input = sys.stdin.readline
N = int(input())
answer = 1
for _ in range(N):
	answer += (int(input()) - 1)
print(answer)
