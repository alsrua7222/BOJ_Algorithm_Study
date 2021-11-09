import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
if M == 0:
    print(0)
    exit(0)

arr.sort()
x, y = 0, 0
answer = 2 * 10**9 + 1
while x < N and y < N:
    if M > arr[y] - arr[x]:
        y += 1
    else:
        answer = min(answer, arr[y] - arr[x])
        x += 1
print(answer)
