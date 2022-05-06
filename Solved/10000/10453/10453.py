import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    a = list(a)
    b = list(b)

    a2 = []
    b2 = []
    for i in range(len(a)):
        if a[i] == 'a':
            a2.append(i)
        if b[i] == 'a':
            b2.append(i)

    if len(a2) != len(b2):
        print(-1)
    else:
        answer = 0
        for i in range(len(a2)):
            answer += abs(a2[i] - b2[i])
        print(answer)