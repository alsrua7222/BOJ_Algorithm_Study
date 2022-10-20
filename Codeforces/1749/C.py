import sys
input = sys.stdin.readline
# 에휴
def upper_bound(nums, target):

    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid 

    return right

def solve(n, a):
    if n == 1:
        if a[0] == 1:
            return 1
        else:
            return 0
    
    left, right = 0, n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        tmp = set(a)
        flag = True
        for i in range(1, mid + 1):
            index = upper_bound(a, mid - i + 1)
            if index == a[0]:
                flag = False
                break
            else:
                index -= 1
                tmp.remove(index)
                tmp.remove(tmp[0])
                a = sorted(list(tmp) + [mid + i - 1])
        if flag:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer
                

for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(solve(n, a))