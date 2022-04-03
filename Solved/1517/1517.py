# 풀이 과정
# https://blog.naver.com/alsrua7222/222690539754

import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
answer = 0
def merge(arr1, arr2):
    global answer
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            answer += len(arr1) - i
            result.append(arr2[j])
            j += 1
    
    if i < len(arr1):
        result += arr1[i:]

    if j < len(arr2):
        result += arr2[j:]

    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

mergeSort(A)
print(answer)