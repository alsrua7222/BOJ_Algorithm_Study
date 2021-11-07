find = input()
N = int(input())
answer = 0
def IsAble(str1, start):
    i, cur = start, 0
    while cur != len(find):
        if find[cur] != str1[i % len(str1)]:
            return False
        cur += 1
        i += 1
    return True
for _ in range(N):
    comp = input()
    if len(comp) < len(find):
        continue
    for i in range(len(comp)):
        if IsAble(comp, i):
            answer += 1
            break
print(answer)
