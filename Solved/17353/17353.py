import sys, math
input = sys.stdin.readline
N = int(input())
arr = [0]
arr += list(map(int, input().split()))
size = int(math.ceil(math.log2(N))) + 1
tree = [0] * (1 << size)
counts = [0] * (1 << size)

def update(index, value):
    while index <= N:
        tree[index] += value
        if value > 0:
            counts[index] += 1
        else:
            counts[index] -= 1
        index += (index & -index)
    return

def getCount(index):
    answer = [0, 0]
    while index > 0:
        answer[0] += tree[index]
        answer[1] += counts[index]
        index -= (index & -index)
    return answer

answer = ""
for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        update(cmd[1], cmd[1])
        update(cmd[2] + 1, -cmd[1])
    else:
        tmp = getCount(cmd[1])
        answer = answer + str((tmp[1] * (cmd[1] + 1) - tmp[0] + arr[cmd[1]])) + '\n'
print(answer)
