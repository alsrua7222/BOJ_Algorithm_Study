def solution(arr):
    first = 0
    for first in range(len(arr)):
        if arr[first] == 2:
            break
    
    if arr[first] != 2:
        return [-1]
    
    second = first
    for second in range(len(arr) - 1, first - 1, -1):
        if arr[second] == 2:
            break
    
    if first == second:
        return [2]
    
    return arr[first:second + 1]