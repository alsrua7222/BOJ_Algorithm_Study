Debug = 0

N, M = map(int, input().split())
birds = []
eachSum = [0] * M
for i in range(N):
    dir, string = input().split()
    birds.append([dir, string])
    flag = 1 if dir == 'R' else -1
    for j in range(M):
        if string[j] == '1':
            eachSum[j] += flag

prefixSum = [eachSum[0]]
for j in range(1, M):
    prefixSum.append(prefixSum[-1] + eachSum[j])

if Debug:
    print(prefixSum)

answer = float('inf')
num = float('inf')
for i in range (N):
    dir, string = birds[i]
    flag = -1 if dir == 'R' else 1
    pre = 0
    absMax = 0
    if Debug:
        print(f"bird {i}, dir={dir}, string={string}")
    for j in range(M):
        if string[j] == '1':
            pre += flag
        absMax = max(absMax, abs(prefixSum[j] + pre))
        if Debug:
            print(f"pre={pre}, prefixSum[{j}]={prefixSum[j]}, absMax={absMax}")
    if answer > absMax:
        answer = absMax
        num = i + 1
    elif answer == absMax:
        num = min(num, i + 1)

print(num, answer, sep="\n")