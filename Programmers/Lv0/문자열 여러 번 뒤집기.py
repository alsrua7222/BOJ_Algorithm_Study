def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    for s, e in queries:
        my_string[s:e + 1] = my_string[s:e + 1][::-1]
    return "".join(my_string)