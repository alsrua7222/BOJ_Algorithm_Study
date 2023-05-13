def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        ret = float('inf')
        for v in arr[s:e + 1]:
            if k < v:
                ret = min(ret, v)
        answer.append(ret if ret != float('inf') else -1)
    return answer