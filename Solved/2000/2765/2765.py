cnt = 1
while True:
    rad, rpm, times = map(float, input().split())
    if rpm == 0:
        break

    r_mile = rad / 12 / 5280
    h_time = times / 60 / 60

    d = rpm * 3.1415927 * r_mile
    v = d / h_time
    print("Trip #{}: {:.2f} {:.2f}".format(cnt, d, v))
    cnt += 1