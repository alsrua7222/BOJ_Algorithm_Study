for _ in range(int(input())):
    string = list(input())

    # 1
    left = 0
    for i in range(1, len(string)):
        if string[i] > string[i - 1]:
            if left < i:
                left = i
    
    # 2
    right = 1
    for i in range(1, len(string)):
        if string[i] > string[left - 1]:
            if right < i:
                right = i
    
    if left != 0 and right != 0:
        string[left - 1], string[right] = string[right], string[left - 1]
        string[left:] = list(string[left:][::-1])
    print(''.join(string))