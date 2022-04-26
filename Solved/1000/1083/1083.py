N = int(input())
arr = list(map(int, input().split()))
cut = int(input())

for i in range(N):
    cur = arr[i]
    max_idx = i
    MAX = arr[i]

    for i2 in range(i, min(i + cut + 1, N)):
        if cur < arr[i2] and MAX < arr[i2]:
            MAX = arr[i2]
            max_idx = i2
    cost = max(0, max_idx - i)
    if cost <= cut:
        if i != max_idx:
            cut -= cost
            arr = arr[:i] + [arr[max_idx]] + arr[i:max_idx] + arr[max_idx + 1:]
            if cut == 0:
                break

print(*arr)