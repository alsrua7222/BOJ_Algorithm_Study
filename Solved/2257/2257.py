# 풀이 과정
# https://blog.naver.com/alsrua7222/222626349774

str1 = input()
answer = []
info = {'H': 1, 'C': 12, 'O': 16}
for v in str1:
    if v in info:
        answer.append(info[v])
    elif v == '(':
        answer.append(v)
    elif v == ')':
        total = 0
        while answer:
            tmp = answer.pop()
            if tmp == '(':
                answer.append(total)
                break
            else:
                total += tmp

    else:
        answer[-1] *= int(v)

print(sum(answer))