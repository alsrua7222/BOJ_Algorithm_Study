import sys
input = sys.stdin.readline
S = input().rstrip()
pS = [[0 for i in range(26)]]
for i in range(len(S)):
    a_idx = ord(S[i]) - ord('a')
    tmp = pS[-1].copy()
    tmp[a_idx] += 1
    pS.append(tmp)

for i in range(int(input())):
    a, l, r = input().split()
    l, r = map(int, [l, r])
    
    print(pS[r + 1][ord(a) - ord('a')] - pS[l][ord(a) - ord('a')])