import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(arr, start, visited, goal):
    if arr[start] in goal:
        visited[arr[start]] = 2
        visited[start] = 2
        return True
    if visited[start] >= 1:
        return False
    visited[start] = 1
    goal.add(start)
    if DFS(arr, arr[start], visited, goal):
        if visited[start] != 2:
            visited[start] = 2
            return True
        else:
            return False

for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    answer = 0
    visited = [0] * (N + 1)

    # 자기 선택한 경우, 같은 싸이클 방지를 위해 먼저 처리.
    for i in range(1, N + 1):
        if arr[i] == i:
            answer += 1
            visited[i] = 2

    # 자기 번호를 찾으면 싸이클한 횟수만큼 visited에 1 대신 2로 처리. 
    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            set1 = set()
            set1.add(i)
            if DFS(arr, arr[i], visited, set1):
                visited[i] = 2
    answer = 0
    for v in visited[1:]:
        if v == 1:
            answer += 1
    print(answer)
