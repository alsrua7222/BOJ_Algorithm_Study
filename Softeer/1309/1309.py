import sys
input = sys.stdin.readline

N = int(input())
ranks = []
for _ in range(3):
    results = []
    info = dict()
    inputs = list(map(int, input().split()))
    for v in inputs:
        if v in info:
            info[v] += 1
        else:
            info[v] = 1
    
    info_sort = sorted(info.items(), key=lambda x: (-x[0]))
    print(info_sort)
    ranks.append(results)
