from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    color = ['-1'] + list(input().rstrip())
 
    answer = 0
 
    Tree = defaultdict(list)
    for i in range(n - 1):
        Tree[a[i]].append(i + 2)
 
    def DFS(node):
        global answer
        if not Tree[node]: # leaf end node
            if color[node] == 'B':
                return [1, 0]
            else:
                return [0, 1]
        
        B, W = 0, 0
        if color[node] == 'B':
            B += 1
        else:
            W += 1
 
        for child in Tree[node]:
            b, w = DFS(child)
            B += b
            W += w

        if B == W:
            answer += 1
        return [B, W]
    DFS(1)
    print(answer)