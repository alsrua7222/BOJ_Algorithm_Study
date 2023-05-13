str = input()
result = ""
for c in str:
    if c.isupper():
        result += c.lower()
    else:
        result += c.upper()
print(result)