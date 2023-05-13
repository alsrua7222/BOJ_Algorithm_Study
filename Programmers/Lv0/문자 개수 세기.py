def solution(my_string):
    answer = [0] * 52
    for ch in my_string:
        if ch.isupper():
            answer[ord(ch) - ord('A')] += 1
        else:
            answer[26 + ord(ch) - ord('a')] += 1
        
    return answer