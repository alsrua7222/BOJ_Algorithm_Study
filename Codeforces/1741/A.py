import sys
input = sys.stdin.readline

for tc in range(int(input())):
    a, b = input().split()
    if a[-1] != b[-1]:
        if a[-1] == 'S':
            print('<')
        elif a[-1] == 'M':
            print('<' if b[-1] == 'L' else '>')
        else:
            print('>')
    else:
        if len(a) > len(b):
            if a[-1] == 'S':
                print('<')
            else:
                print('>')
        elif len(a) < len(b):
            if a[-1] == 'S':
                print('>')
            else:
                print('<')
        else:
            print('=')