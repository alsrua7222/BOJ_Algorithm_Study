def solution(my_strings, parts):
    answer = ''
    for idx in range(len(parts)):
        word = my_strings[idx]
        s, e = parts[idx]
        
        answer += word[s:e+1]
    return answer