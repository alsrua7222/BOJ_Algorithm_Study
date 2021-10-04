def IsPelindrom(str1):
    for i in range(len(str1) // 2):
        if str1[i] != str1[-(i + 1)]:
            return False
    return True


while True:
    str1 = input()
    if str1 == '0':
        break
    if IsPelindrom(str1):
        print("yes")
    else:
        print("no")
