from collections import deque, defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    flags = [-1] * (V + 1)
    Graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        Graph[u].append(v)
        Graph[v].append(u)
    
    def BFS(start, flag):
        Queue = deque([[start, flag]])
        flags[start] = flag
        while Queue:
            s, f = Queue.popleft()
            for node in Graph[s]:
                if flags[node] == f:
                    return False
                if flags[node] == -1:
                    flags[node] = f ^ 1
                    Queue.append([node, f ^ 1])
        return True
        
    success = True
    for start in range(1, V + 1):
        if flags[start] == -1 and not BFS(start, 1):
            success = False
            break
    print("YES" if success else "NO")
