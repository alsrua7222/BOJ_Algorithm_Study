from itertools import combinations
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
moums = ['a', 'e', 'i', 'o', 'u']
for v in combinations(arr, L):
    cnt = 0
    for moum in moums:
        if moum in v:
            cnt += 1
    if cnt >= 1 and L - cnt >= 2:
        print("".join(v))