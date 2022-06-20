# 왜 12자리수로 나눠줘야하는지 아직도 모르겠음.

N = int(input())
answer = 1
for i in range(1, N + 1):
    answer *= i
    while answer % 10 == 0:
        answer //= 10
    answer = answer % 10 ** 12

print(str(answer % 100000).rjust(5, '0'))