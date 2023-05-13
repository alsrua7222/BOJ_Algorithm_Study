def solution(my_string, is_suffix):
    answer = 0
    my_string = my_string[::-1]
    is_suffix = is_suffix[::-1]
    if len(is_suffix) > len(my_string):
        return 0
    
    for i in range(len(is_suffix)):
        if is_suffix[i] != my_string[i]:
            return 0
    return 1