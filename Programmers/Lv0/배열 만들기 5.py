def solution(intStrs, k, s, l):
    answer = []
    for string in intStrs:
        sub = int(string[s:s + l])
        if sub > k:
            answer.append(sub)
    return answer