N, K, T, U, V, L = map(int, input().split())
carrot_info = set(int(input()) for _ in range(N))

bag = 0
answer = 0
speed_time = 0

for cur in range(1, L + 1):
    if speed_time >= 1:
        speed_time -= 1
        answer += 1 / V
    elif bag:
        bag -= 1
        speed_time = T * V - 1
        answer += 1 / V
    else:
        answer += 1 / U

    if cur in carrot_info:
        if bag != K:
            bag += 1
        else:
            speed_time = T * V

print("{:.12f}".format(answer))