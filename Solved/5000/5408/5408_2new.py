from math import log
import sys
input = sys.stdin.readline
def solve(alphabets, errors, trans, message):
    result = [0] * len(alphabets)
    pre_result = [0] * len(alphabets)
    prev = [[0] * len(alphabets) for _ in range(300)]
    
    for i in range(len(alphabets)):
        # result[i] = errors[alphabets.index(message[0])][i]
        result[i] = errors[i][alphabets.index(message[0])]
        prev[0][i] = -1

    for i in range(1, len(message)):
        result, pre_result = pre_result, result
        
        for j in range(len(alphabets)):
            result[j] = 1
            prev[i][j] = -1
        curCharIdx = alphabets.index(message[i])
        
        for j in range(len(alphabets)):
            for k in range(len(alphabets)):
                # if pre_result[j] > 0 or trans[j][k] > 0 or errors[curCharIdx][k] > 0:
                #     continue
                # prob = pre_result[j] + trans[j][k] + errors[curCharIdx][k]
                if pre_result[j] > 0 or trans[j][k] > 0 or errors[k][curCharIdx] > 0:
                    continue
                prob = pre_result[j] + trans[j][k] + errors[k][curCharIdx]
                if prob > result[k] or result[k] > 0:
                    result[k] = prob
                    prev[i][k] = j
    
    node = -1
    prob = 1

    for i in range(len(alphabets)):
        if prob > 0 or (0 >= result[i] > prob):
            prob = result[i]
            node = i
    
    tmp = [0] * len(message)
    idx = len(message) - 1

    tmp[idx] = node
    while idx > 0:
        node = prev[idx][node]
        idx -= 1
        tmp[idx] = node
    
    answer = ""
    for i in range(len(message)):
        answer += alphabets[tmp[i]]
    return answer

# file = open("out.out", "w")
for _ in range(int(input())):
    ac = int(input())
    alphabets = list(input().split())
    
    errors = []
    for _ in range(ac):
        tmp = list(map(float, input().split()))
        tmp2 = []
        for v in tmp:
            if v > 0:
                tmp2.append(log(v))
            else:
                tmp2.append(1)
        errors.append(tmp2)
        # errors.append(list(map(log, list(map(float, input().split())))))
    
    trans = []
    for _ in range(ac):
        tmp = list(map(float, input().split()))
        tmp2 = []
        for v in tmp:
            if v > 0:
                tmp2.append(log(v))
            else:
                tmp2.append(1)
        trans.append(tmp2)
        # trans.append(list(map(log, list(map(float, input().split())))))

    for _ in range(int(input())):
        message = input().rstrip()
        print(solve(alphabets, errors, trans, message))
        # file.write(solve(alphabets, errors, trans, message) + "\n")
# file.close()