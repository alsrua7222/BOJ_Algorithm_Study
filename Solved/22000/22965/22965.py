import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
MIN = [float("inf"), 0]

# 최솟값과 인덱스 찾기.
for i in range(N):
    if MIN[0] > arr[i]:
        MIN = [arr[i], i]

cur = 0
success = True
for i in range(N):
    if cur < arr[(i + MIN[1]) % N]:
        cur = arr[(i + MIN[1]) % N]
    else:
        success = False
        break

if success:
    if MIN[1] == 0:
        print(1)
    else:
        print(2)
else:
    print(3)
