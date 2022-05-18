import sys; input = sys.stdin.readline
w, h, n = map(int, input().split())
xs, ys, rs = [], [], []
for _ in range(n):
    x, y, r = map(int, input().split())
    xs.append(x)
    ys.append(y)
    rs.append(r)

answer = 0
# 0부터 h까지 가능한 경우를 탐색
for i in range(h):
    collects = []
    for j in range(n):
        # 길이가 원 반지름보다 짧아야 함.
        rad_y = abs(ys[j] - i)
        if rad_y <= rs[j]:
            rad_x = int((rs[j] ** 2 - rad_y ** 2) ** .5)
            collects.append(max(0, xs[j] - rad_x) * 2)
            collects.append(min(w - 1, xs[j] + rad_x) * 2 + 1)
    
    # 오름차순
    collects.sort()
    cnt, pre = 0, 0

    for v in collects:
        # # Debug
        # print(i, v, cnt, pre)
        cur = v // 2
        if v % 2 == 0:
            cnt += 1
            if cnt == 1:
                pre = cur
        else:
            cnt -= 1
            if cnt == 0:
                answer += cur - pre + 1

print(w * h - answer)
