def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        c = code[idx]
        if c == '1':
            mode = 0 if mode else 1
        else:
            if mode == 1 and idx & 1:
                answer += c
            elif mode == 0 and idx & 1 == 0:
                answer += c

    return answer if answer != "" else "EMPTY"