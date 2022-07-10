import sys
input = sys.stdin.readline
for _ in range(int(input())):
    w = input().rstrip()
    w2 = []
    for i in range(len(w)):
        w2.append([w[i], i])
    w2.sort()

    p = int(input())
    total = 0
    index = 0
    arr = []
    while total <= p and index < len(w):
        total += (ord(w2[index][0]) - ord('a') + 1)
        if total > p:
            break
        arr.append(w2[index])
        index += 1
    arr.sort(key=lambda x: x[1])
    answer = ""
    for v in arr:
        answer += v[0]
    print(answer)