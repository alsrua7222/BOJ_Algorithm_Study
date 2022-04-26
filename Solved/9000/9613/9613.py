def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    tmp = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tmp += gcd(arr[i], arr[j])
    print(tmp)
