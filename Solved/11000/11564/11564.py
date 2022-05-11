k, a, b = map(int, input().split())
answer = 0

if a <= 0 and b <= 0:
    answer += -a // k
    answer -= -b // k
    if -b % k == 0:
        answer += 1
elif a <= 0 and b >= 0:
    answer += - a // k
    answer += b // k
    answer += 1
elif a >= 0 and b >= 0:
    answer += b // k
    answer -= a // k
    if a % k == 0:
        answer += 1
print(answer)