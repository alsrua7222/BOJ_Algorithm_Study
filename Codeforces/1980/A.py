import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    arr = input().strip()
    dict1 = {ch : 0 for ch in "ABCDEFG"}
    for ch in arr:
        if ch in dict1:
            dict1[ch] += 1
    
    answer = 0
    for ch in "ABCDEFG":
        if dict1[ch] < m:
            answer += (m - dict1[ch])
    print(answer)