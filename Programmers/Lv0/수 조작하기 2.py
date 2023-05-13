def solution(numLog):
    answer = ''
    for i in range(len(numLog) - 1):
        status = numLog[i + 1] - numLog[i]
        if status == 1:
            answer += 'w'
        elif status == -1:
            answer += 's'
        elif status == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer