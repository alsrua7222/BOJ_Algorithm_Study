N = int(input())
tiles = [1, 2, 3]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if N / 2 <= a:
        a = N - a + 1
    if N / 2 <= b:
        b = N - b + 1
    print(tiles[(min(a, b) - 1) % 3])
