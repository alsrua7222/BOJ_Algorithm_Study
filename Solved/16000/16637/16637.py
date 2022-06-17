import sys
sys.setrecursionlimit(10**6)
N = int(input())
s = list(input())
for i in range(0, N, 2):
    s[i] = int(s[i])

answer = -float('inf')
def operate(f, s, op):
    if op == '+':
        return f + s
    elif op == '-':
        return f - s
    elif op == '*':
        return f * s

def dfs(cur, total):
    global answer
    if cur >= N - 1:
        answer = max(answer, total)
        return
    
    if cur + 2 < N:
        dfs(cur + 2, operate(total, s[cur + 2], s[cur + 1]))
    
    if cur + 4 < N:
        dfs(cur + 4, operate(total, operate(s[cur + 2], s[cur + 4], s[cur + 3]), s[cur + 1]))
    
    return

dfs(0, s[0])
print(answer)