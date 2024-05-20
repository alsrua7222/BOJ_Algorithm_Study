import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = list(input().strip())
    index_list = sorted(set(s))
    index_dict = {}
    for i in range(len(index_list)):
        index_dict[index_list[i]] = i
    index_list = index_list[::-1]

    print(''.join([index_list[index_dict[s[i]]] for i in range(n)]))