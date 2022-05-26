N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = []
for s, i, c in arr:
    arr2 += list(s + i * cnt for cnt in range(c))
arr2.sort()

if T <= arr2[0]:
    answer = arr2[0] - T
elif T > arr2[-1]:
    answer = -1
else:
    left = 0
    right = len(arr2) - 1
    while left < right:
        mid = (left + right) // 2
        if arr2[mid] < T:
            left = mid + 1
        else:
            right = mid
    answer = arr2[right] - T

print(answer)