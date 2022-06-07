str1 = ""
for v in input():
    if v.isupper():
        str1 += v.lower()
    else:
        str1 += v.upper()
print(str1)