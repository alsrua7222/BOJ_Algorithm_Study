n = int(input())
a = list(map(int, input().split()))
a.sort()
answer = 0
tmp = a[0]

if n <= 2:
    if n == 1:
        print(tmp)
    else:
        if a[0] + 1 == a[1]:
            print(a[0])
        else:
            print(a[0] + a[1])
    exit(0)

for i in range(n - 1):
    if a[i] + 1 == a[i + 1]:
        continue
    else:
        answer += tmp
        tmp = a[i + 1]
answer += tmp

print(answer)