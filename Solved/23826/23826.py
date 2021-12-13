import sys
input = sys.stdin.readline
N = int(input())
arr = []
answer = []
X, Y, E = map(int, input().split())
for i in range(N):
    arr.append(list(map(int, input().split())))
    answer.append(max(0, E - (abs(arr[i][0] - X) + abs(arr[i][1] - Y))) - arr[i][2])
    for j in range(i):
        answer[j] -= max(0, arr[i][2] - (abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])))
        answer[i] -= max(0, arr[j][2] - (abs(arr[j][0] - arr[i][0]) + abs(arr[j][1] - arr[i][1])))
MAX = 0
for v in answer:
    if v < 0:
        print("IMPOSSIBLE")
        exit(0)
    elif v > MAX:
        MAX = v
print(MAX if MAX != 0 else "IMPOSSIBLE")
