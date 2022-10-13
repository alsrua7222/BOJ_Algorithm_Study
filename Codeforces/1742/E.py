import sys
input = sys.stdin.readline
"""
TLE 뜰 것 같아서 C++로 바꿈.
"""
def solve(n, q, a, k):
    def binsearch(arr, left, right, target):
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right
    
    answer = []
    prefixSum = [0]
    prefixMax = [0]
    for i in range(1, n + 1):
        prefixSum.append(prefixSum[-1] + a[i - 1])
        prefixMax.append(max(prefixMax[-1], a[i - 1]))
    
    for i in range(q):
        answer.append(prefixSum[binsearch(prefixMax, 0, n - 1, k[i])])

    return answer

for tc in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))

    print(*solve(n, q, a, k))