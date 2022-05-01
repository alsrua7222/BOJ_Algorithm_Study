from collections import deque
N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

Queue = deque([[0, A.copy()]])
visited = set()
visited.add(tuple(A))
answer = -1
while Queue:
    score, arr = Queue.popleft()
    if is_sorted(arr):
        answer = score
        break

    for i in range(len(arr) - K + 1):
        tmp = arr[:i] + arr[i:i+K][::-1] + arr[i+K:]
        if tuple(tmp) in visited:
            continue
        visited.add(tuple(tmp))
        Queue.append([score + 1, arr[:i] + arr[i:i+K][::-1] + arr[i+K:]])
print(answer)