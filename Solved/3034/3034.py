N, W, H = map(int, input().split())
MAX = (W ** 2 + H ** 2)
for _ in range(N):
    if int(input()) ** 2 <= MAX:
        print('DA')
    else:
        print('NE')
