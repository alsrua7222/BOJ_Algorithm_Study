# 풀이 과정
# https://blog.naver.com/alsrua7222/222710151191

N = int(input())
Graph = [0] + [int(input()) for _ in range(N)]
visited = [0] * (N + 1)
visit = 0
collect = []
def DFS(cur, parent, root):
    if cur == parent and not root:
        return True
    if visited[cur] != visit:
        visited[cur] = visit
        collect.append(cur)
        if DFS(Graph[cur], parent, False):
            return True
    return False

answer = []
for i in range(1, N + 1):
    visit += 1
    collect = []
    if DFS(i, i, True):
        answer += collect

answer = sorted(list(set(answer)))
print(len(answer))
print(*answer, sep="\n")