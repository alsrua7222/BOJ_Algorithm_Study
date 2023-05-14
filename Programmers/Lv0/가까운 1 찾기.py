def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i]:
            return i
    return -1