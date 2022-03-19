# 풀이 과정
# https://blog.naver.com/alsrua7222/222677282286

str1 = input()
stack = [0]
answer = 0
cnt = 0
for i in range(len(str1)):
    if str1[i] == '(':
        stack.append(stack[-1] + 1)
    else:
        if str1[i - 1] == ')':
            stack.pop()
            cnt += 1
            continue
        stack.pop()
        answer += stack[-1]
print(answer + cnt)