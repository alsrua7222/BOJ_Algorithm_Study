arr = list(map(int, input().split()))

def IsASC():
    tmp = 0
    for v in arr:
        if v > tmp:
            tmp = v
        else:
            return False
    return True

def IsDESC():
    tmp = 9
    for v in arr:
        if v < tmp:
            tmp = v
        else:
            return False
    return True

if IsASC():
    print("ascending")
elif IsDESC():
    print("descending")
else:
    print("mixed")
