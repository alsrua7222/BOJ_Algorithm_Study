import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
# N 최대가 50만 이므로, O(N^2), O(N^2 / 2)로 풀리지 않는다.
# 그러면 O(NlogN)으로 내버려야 한다.
arr.sort()
arr2 = []
total = sum(arr)
arr2.append(total)
for i in range(1, N):
    arr2.append(arr2[-1] - arr[i - 1])
answer = 0
for i in range(N):
    answer += (arr2[i] - (N - i) * arr[i]) * 2
print(answer)
