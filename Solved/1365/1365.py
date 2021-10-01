import sys,bisect
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
visited = [arr[0]]
cnt = 1

for i in range(1, N):
    if arr[i] > visited[cnt - 1]:
        visited.append(arr[i])
        cnt += 1
    else:
        index = bisect.bisect_left(visited, arr[i])
        visited[index] = arr[i]
print(N - cnt)
