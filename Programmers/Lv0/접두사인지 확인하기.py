def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string):
        return 0
    
    for i in range(len(is_prefix)):
        if is_prefix[i] != my_string[i]:
            return 0
    return 1