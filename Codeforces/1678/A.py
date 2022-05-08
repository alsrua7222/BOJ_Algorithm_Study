import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    count_0 = 0
    for v in a:
        if v == 0:
            count_0 += 1
    
    IsSame = False
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j] and a[i] != 0:
                IsSame = True
                break
        if IsSame:
            break
    
    if count_0 == 0:
        print(n + (1 if not IsSame else 0))
    else:
        answer = 0
        for v in a:
            if v != 0:
                answer += 1
        print(answer)