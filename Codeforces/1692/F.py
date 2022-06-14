from collections import defaultdict
import sys
input = sys.stdin.readline

def getNumber(f, s):
    if (f + s) % 10 <= 3:
        return 3 - (f + s) % 10
    else:
        return 13 - (f + s) % 10

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dict1 = defaultdict(list)
    for i in range(n):
        dict1[a[i] % 10].append(i)
    
    success = False

    for i in range(10):
        if not dict1[i]:
            continue

        for index1 in dict1[i]:
            used = set()
            used.add(index1)
            for j in range(10):
                if (not dict1[j]) or (not dict1[getNumber(i, j)]):
                    continue

                for index2 in dict1[j]:
                    if index2 in used:
                        continue

                    used.add(index2)
                    for index3 in dict1[getNumber(i, j)]:
                        if index3 in used:
                            continue

                        success = True
                        break
                    if success:
                        break
                    else:
                        used.remove(index2)
            if success:
                break
        if success:
            break
    if success:
        print("YES")
    else:
        print("NO")