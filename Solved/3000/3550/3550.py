string = input()
answer = ""
for v in string:
    if v.isdigit():
        answer += f"({v})+"
    else:
        answer += '(0)+'
print(answer + '0')