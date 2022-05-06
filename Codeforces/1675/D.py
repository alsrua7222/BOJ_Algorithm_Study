# 아무리 해봐도 결국 코드포스에서는 재귀 깊이를 설정 못 한다.
# 파이썬 똥똥똥

import sys
sys.setrecursionlimit(2 * (10 ** 5))
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    Graph = dict()
    root = -1
    for i in range(n):
        if a[i] == i + 1:
            root = i + 1
        else:
            if a[i] in Graph:
                Graph[a[i]].append(i + 1)
            else:
                Graph[a[i]] = [i + 1]
    
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
        index = 0
        try:
            while index < len(Graph[node]):
                child = Graph[node][index]
                if visited[child]:
                    continue
                dfs(child)
                index += 1
        except Exception as e:
            print(e)
            print("node: ", node)
            print("Graph:", Graph[node])
        return

    dfs(root)
    print(len(answer))
    for v in answer:
        if len(v) == 0:
            continue
        print(len(v))
        print(*v)
    print()