def solution(num_list):
    answer = 0
    multi = 1
    squre = 0
    for v in num_list:
        multi *= v
        squre += v
    return 1 if multi < squre ** 2 else 0