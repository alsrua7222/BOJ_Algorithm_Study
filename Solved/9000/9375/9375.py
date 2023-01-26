def solve():
    n = int(input())
    info = dict()
    for _ in range(n):
        name, type = input().split()
        if type not in info:
            info[type] = 1
        info[type] += 1
    
    answer = 1
    for v in info.values():
        answer *= v
    print(answer)
for T in range(int(input())):
    solve()