def isPrime(n):
    if n == 1 or (n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def process(n, k):
    ret = ""
    while n > 0:
        ret += str(n % k)
        n //= k
    return ret[::-1].split('0')

def solution(n, k):
    answer = 0
    for value in process(n, k):
        if value and isPrime(int(value)):
            answer += 1
    return answer