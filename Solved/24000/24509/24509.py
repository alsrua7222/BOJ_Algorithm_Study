# https://blog.naver.com/alsrua7222/222653172341
import sys
input = sys.stdin.readline
N = int(input())
arr = [list() for _ in range(N)]
for _ in range(N):
    n, a, b, c, d = map(int, input().split())
    arr[0].append([a, n])
    arr[1].append([b, n])
    arr[2].append([c, n])
    arr[3].append([d, n])

for i in range(4):
    arr[i].sort(key=lambda x: (-x[0], x[1]))
used = set()
def solve(arr1):
    for v, i in arr1:
        if i not in used:
            used.add(i)
            return i
    return 0

answer = [0] * 4
for i in range(4):
    answer[i] = solve(arr[i])
print(*answer)
