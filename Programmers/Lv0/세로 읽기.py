def solution(my_string, m, c):
    answer = ["" for i in range(len(my_string) // m)]
    for i in range(0, len(my_string) // m):
        answer[i] = my_string[i * m:(i + 1) * m]
    
    result = ""
    for r in range(len(answer)):
        result += answer[r][c - 1]
    return result