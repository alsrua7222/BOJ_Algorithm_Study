import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
seg_dp = [arr[0]]
index_arr = [0]
index = 1
for i in range(1, N):
    if seg_dp[-1] < arr[i]:
        seg_dp.append(arr[i])
        index_arr.append(index)
        index += 1
    else:
        end = len(seg_dp)
        start = 0
        while start < end:
            mid = (start + end) // 2
            if seg_dp[mid] < arr[i]:
                start = mid + 1
            else:
                end = mid
        seg_dp[end] = arr[i]
        index_arr.append(end)

# 역 추적
print(len(seg_dp))
answer = []
cnt = len(seg_dp) - 1
for i in range(N - 1, -1, -1):
    if cnt == index_arr[i]:
        answer.append(arr[i])
        cnt -= 1
print(' '.join(map(str, answer[::-1])))
