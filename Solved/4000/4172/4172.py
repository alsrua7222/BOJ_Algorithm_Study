import math
x = [1]
while True:
    n = int(input())
    if n == -1:
        break

    for i in range(len(x), n + 1):
        a = int(i - i ** 0.5)
        b = int(math.log(i, math.e))
        c = int(i * (math.sin(i) ** 2))
        # print(f"i = {i}, ", x[a], x[b], x[c])
        x.append((x[a] + x[b] + x[c]) % 1000000)

    print(x[n])