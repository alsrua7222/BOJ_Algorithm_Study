N, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
print(a[k - 1])