import sys
input = sys.stdin.readline
"""
Comment
Python3으로 제출하면 TLE
pypy-64로 제출하면 Accept

파이썬 당했다... ㅠㅠ
"""
def merge_sort(arr):
    answer = [0, True]
    def sort(low, high):
        if not answer[1]:
            return
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        if not answer[1]:
            return
        temp = []
        l, h = low, mid

        # while l < mid and h < high:
        #     if arr[l] < arr[h]:
        #         temp.append(arr[l])
        #         l += 1
        #     else:
        #         temp.append(arr[h])
        #         h += 1

        if arr[l] < arr[h]:
            while l < mid:
                temp.append(arr[l])
                l += 1
            while h < high:
                temp.append(arr[h])
                h += 1
        else:
            answer[0] += 1
            while h < high:
                temp.append(arr[h])
                h += 1
            while l < mid:
                temp.append(arr[l])
                l += 1
            
        pre = temp[0]
        if temp[1] - temp[0] != 1:
            answer[1] = False
        
        for i in range(len(temp)):
            arr[low + i] = temp[i]
            if i != 0:
                if temp[i] - pre == 1:
                    pre = temp[i]
                else:
                    answer[1] = False
                    return
            
    mergearr = sort(0, len(arr))
    return answer[0] if answer[1] else -1

for tc in range(int(input())):
    m = int(input())
    a = list(map(int, input().split()))
    print(merge_sort(a))