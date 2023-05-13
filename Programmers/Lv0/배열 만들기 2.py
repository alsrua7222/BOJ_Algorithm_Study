def solution(l, r):
    answer = []
    for cur in range(l, r + 1):
        flag = True
        for c in str(cur):
            if c not in '05':
                flag = False
                break
        
        if flag:
            answer.append(cur)
    return answer if answer else [-1]