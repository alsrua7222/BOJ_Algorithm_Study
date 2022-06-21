S = list(input())
if S == S[::-1]:
    print(len(S))
else:
    answer = 0
    for i in range(len(S)):
        s = S + S[:i + 1][::-1]
        if s == s[::-1]:
            answer = len(s)
            break
    print(answer)