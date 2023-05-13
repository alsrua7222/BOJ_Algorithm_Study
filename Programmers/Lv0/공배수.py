def solution(number, n, m):
    answer = 0 if number % n or number % m else 1
    return answer