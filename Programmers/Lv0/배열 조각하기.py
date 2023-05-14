from collections import deque
def solution(arr, query):
    arr = deque(arr)
    for i in range(len(query)):
        if i & 1:
            for _ in range(query[i]):
                arr.popleft()
        else:
            for _ in range(len(arr) - query[i] - 1):
                arr.pop()
    return list(arr)
                