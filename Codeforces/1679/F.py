from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    dict1 = defaultdict(int)
    vector = []
    
    for v in a:
        dict1[v] += 1
        if dict1[v] == k:
            vector.append(v)
    
    vector.sort()

    answer = -1
    left = 0
    right = 0

    i = 0
    while i < len(vector):
        j = i + 1
        cur = 1
        while j < len(vector) and vector[j] == vector[j - 1] + 1:
            j += 1
            cur += 1
        
        if answer < cur:
            left = vector[i]
            right = vector[j - 1]
            answer = cur
        i = j
    
    if answer == -1:
        print(-1)
    else:
        print(left, right)