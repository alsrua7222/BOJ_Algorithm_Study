N = int(input())
power = 1
answer = 0
while power <= N:
    answer += (N - power + 1)
    power *= 10
print(answer)