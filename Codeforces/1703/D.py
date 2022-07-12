import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    dict1, dict2 = dict(), dict()
    strings = []
    for _ in range(n):
        string = input().rstrip()
        strings.append(string)
        if string not in dict1:
            dict1[string] = 1
        else:
            dict1[string] += 1
        
        dict2[string] = 0
    
    for key in dict1.keys():
        for i in range(1, len(key)):
            s1 = key[0:i]
            s2 = key[i:]
            if s1 in dict1 and s2 in dict1 and dict2[key] == 0:
                dict2[key] = 1
    
    for i in range(n):
        print(dict2[strings[i]], end="")    
    print()