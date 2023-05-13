def solution(ineq, eq, n, m):
    answer = 0
    flag = False
    if eq == "=":
        if n == m:
            return 1
    
    if n < m:
        flag = True
    
    if ineq == ">":
        flag = not flag
    
    return 1 if flag else 0