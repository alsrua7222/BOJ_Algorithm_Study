from collections import deque
array = deque(list(input()))
operator = deque()
answer = ""
Priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
while array:
    tmp = array.popleft()
    if tmp in ['+', '-', '*', '/']:
        while operator:
            if Priority[operator[-1]] >= Priority[tmp]:
                answer += operator.pop()
            else:
                break
        operator += tmp
    elif tmp == '(':
        operator += tmp
    elif tmp == ')':
        oper_top = operator.pop()
        while oper_top != '(':
            answer += oper_top
            oper_top = operator.pop()
    else:
        answer += tmp
while operator:
    answer += operator.pop()
print(answer)
