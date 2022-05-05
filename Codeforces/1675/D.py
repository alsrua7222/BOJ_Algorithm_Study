# 런타임 에러 7번에서 자주 터짐.
# 이유를 전혀 알 수 없음.

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    Graph = defaultdict(list)
    root = -1
    for i in range(n):
        if a[i] == i + 1:
            root = i + 1
        else:
            Graph[a[i]].append(i + 1)
    
    answer = []
    collect = []
    visited = [False] * (n + 1)
    def dfs(node):
        global collect, answer
        collect.append(node)
        visited[node] = True
        
        if node not in Graph:
            answer.append(collect)
            collect = []
            return
        for child in list(Graph[node]):
            if visited[child]:
                continue
            dfs(child)
        return

    dfs(root)
    print(len(answer))
    for v in answer:
        if len(v) == 0:
            continue
        print(len(v))
        print(*v)
    print()