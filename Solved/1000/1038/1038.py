N = int(input())
if N > 1022:
    print(-1)
    exit(0)
# 감소하는 수의 개수가 최대 1023개이다. 즉, 9876543210 그 이상은 없다는 뜻이다.
arr = []
for i in range(1, 1024):
    tmp = 0
    for j in range(9, -1, -1):
        if i % 2 == 1:
            tmp = tmp * 10 + j
        i //= 2
    arr.append(tmp)
arr.sort()
print(arr[N])
