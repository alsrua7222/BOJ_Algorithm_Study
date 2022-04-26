import heapq
N, M = map(int, input().split())
arr = []
for _ in range(N):
    P, L = map(int, input().split())
    tmp = sorted(list(map(int, input().split())), reverse=True)
    if len(tmp) >= L:
        heapq.heappush(arr, tmp[L - 1])
    else:
        heapq.heappush(arr, 1)

answer = 0
cnt = 0
while arr:
    answer += heapq.heappop(arr)
    cnt += 1
    if answer > M:
        cnt -= 1
        break
print(cnt)
