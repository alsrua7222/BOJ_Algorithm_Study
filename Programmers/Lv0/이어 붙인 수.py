def solution(num_list):
    odd = ""
    even = ""
    for v in num_list:
        if v & 1:
            odd += str(v)
        else:
            even += str(v)
    return int(odd) + int(even)