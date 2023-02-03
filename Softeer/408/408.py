# 8단 변속기
# https://softeer.ai/practice/info.do?idx=1&eid=408
import sys
arr = list(map(int, sys.stdin.readline().split()))
arr_sort = sorted(arr)
arr_sort_rev = sorted(arr, reverse=True)
if arr == arr_sort:
    print("ascending")
elif arr == arr_sort_rev:
    print("descending")
else:
    print("mixed")