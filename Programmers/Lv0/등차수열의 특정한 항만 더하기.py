def solution(a, d, included):
    answer = 0
    for idx in range(len(included)):
        if included[idx]:
            answer += a + d * idx
    return answer