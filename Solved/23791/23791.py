# 풀이 과정
# https://blog.naver.com/alsrua7222/222631966302

import sys, bisect
input = sys.stdin.readline

N = int(input())
korea = [0] + list(map(int, input().split()))
western = [0] + list(map(int, input().split()))
def bin_search(arr1, arr2):
    left = 0
    right = i + 1
    while left < right:
        mid = (left + right) // 2
        x = k - mid
        if (1 <= x <= j and arr2[x] <= arr1[mid]) or x <= 0:
            right = mid
        else:
            left = mid + 1
    return right

for _ in range(int(input())):
    i, j, k = map(int, input().split())
    right = bin_search(korea, western)
    cnt = bisect.bisect_right(western[1:j + 1], korea[right])
    if right != i + 1 and cnt == k - right:
        print(1, right)
    else:
        i, j = j, i
        right = bin_search(western, korea)
        print(2, right)