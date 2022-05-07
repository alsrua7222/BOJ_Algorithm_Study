string = ""
for _ in range(int(input()) * 2 - 1):
    string += input()
print(eval(string.replace("/", "//")))