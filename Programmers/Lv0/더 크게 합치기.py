def solution(a, b):
    a, b = str(a), str(b)
    answer = max(int(a+b), int(b+a))
    return answer