# 풀이 과정
# https://blog.naver.com/alsrua7222/222635952177

converts = [
    ["ZERO", "0"],
    ["ONE", "1"],
    ["TWO", "2"],
    ["THREE", "3"],
    ["FOUR", "4"],
    ["FIVE", "5"],
    ["SIX", "6"],
    ["SEVEN", "7"],
    ["EIGHT", "8"],
    ["NINE", "9"]
]
def convertTo(IsStr, str1):
    for _from, _to in converts:
        str1 = str1.replace(_from, _to) if IsStr else str1.replace(_to, _from)
    return str1


def operation(ch, answer, tmp):
    if ch == '+':
        answer += tmp
    elif ch == '-':
        answer -= tmp
    elif ch == 'x':
        answer *= tmp
    else:
        answer /= tmp
        answer = int(answer)
    return answer


str1 = input()
str1 = convertTo(True, str1)

answer, tmp, success, first = 0, 0, True, True
pre = '+'

for i in range(len(str1) - 1):
    if str1[i] in '0123456789':
        tmp = tmp * 10 + int(str1[i])
    elif str1[i] in '+-x/':
        if i - 1 >= 0 and str1[i - 1] in '+-x/':
            success = False
            break
        answer = operation(pre, answer, tmp)
        pre = str1[i]
        tmp = 0
    else:
        success = False
        break

if tmp == 0 or str1[-1] != '=':
    success = False
if success:
    answer = operation(pre, answer, tmp)
    print(str1)
    print(convertTo(False, str(int(answer))))
else:
    print("Madness!")