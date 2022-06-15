answer = -float('inf')
x, y = -1, -1
for i in range(1, 10):
    tmp = list(map(int, input().split()))
    for j in range(1, 10):
        if tmp[j - 1] > answer:
            answer = tmp[j - 1]
            x, y = i, j
print(answer)
print(x, y)