import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    
    answer = 0
    for i in range(0, n, 2):
        if s[i] != s[i + 1]:
            answer += 1
    
    s += '2'
    split_s = []
    pre = s[0]
    for i in range(1, len(s)):
        if s[i] != pre[0]:
            split_s.append([pre[0], len(pre)])
            pre = s[i]
        else:
            pre += s[i]
    
    answer2 = 0
    index = 0
    while index < len(split_s) - 1:
        if split_s[index][1]
        if split_s[index][1] < split_s[index + 1][1]:
            