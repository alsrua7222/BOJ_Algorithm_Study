def solution(n, k):
    answer = []
    for v in range(k, n + 1, k):
        answer.append(v)
    return answer