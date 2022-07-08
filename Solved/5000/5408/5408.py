from collections import defaultdict
from math import log
# import sys
# input = sys.stdin.readline

def indexOf(alphabets, char):
    for i in range(len(alphabets)):
        if char == alphabets[i]:
            return i
    return -1

def solve(alphabets, errors, trans, message):
    result = defaultdict(list)
    
    index = indexOf(alphabets, message[0])
    for i in range(len(alphabets)):
        curChar = alphabets[i]
        tmp = ["", 0, curChar, -float('inf')] # format -> prefixString, prior, curChar, bestProb
        curError = errors[i][index]
        
        if tmp[3] < curError:
            tmp[3] = curError
        
        result[curChar] = tmp
    
    MAX = float('inf')
    
    for msgidx in range(1, len(message)):
        curMsgChar = message[msgidx]
        MsgIndex = indexOf(alphabets, curMsgChar)
        postResult = defaultdict(list)

        for key in result.keys():
            result[key][1] += result[key][3]
            result[key][0] += result[key][2]
            result[key][3] = -float('inf')
            

            curPreChar = result[key][2]
            PreIndex = indexOf(alphabets, curPreChar)
            
            for transIndex in range(len(alphabets)):
                sponChar = alphabets[transIndex]
                totalProb = trans[PreIndex][transIndex] + errors[transIndex][MsgIndex]
                
                tmpResult = []
                if sponChar not in postResult:
                    tmpResult = [result[key][0], result[key][1], sponChar, -float('inf')]
                    postResult[sponChar] = tmpResult
                else:
                    tmpResult = postResult[sponChar]
                
                total_soFar = tmpResult[1] + tmpResult[3]
                cur_totalProb = result[key][1] + totalProb
                
                if total_soFar < cur_totalProb:
                    if cur_totalProb - total_soFar < MAX:
                        MAX = cur_totalProb - total_soFar
                    
                    tmpResult[0] = result[key][0]
                    tmpResult[1] = result[key][1]
                    tmpResult[3] = totalProb
                    postResult[sponChar] = tmpResult
        result = postResult
    
    answerResult = []
    MAXProb = -float('inf')
    for key in result.keys():
        result[key][1] += result[key][3]
        result[key][0] += result[key][2]
        result[key][3] = -float('inf')
        
        totalProb = result[key][1]
        if totalProb > MAXProb:
            MAXProb = totalProb
            answerResult = result[key]
    return answerResult[0]

# 시작
for _ in range(int(input())):
    ac = int(input())
    alphabets = list(input().split())
    # 에러
    errors = []
    for i in range(ac):
        errors.append(list(map(float, input().split())))
        for j in range(len(errors[i])):
            errors[i][j] = log(errors[i][j])
    
    # 변환
    trans = []
    for i in range(ac):
        trans.append(list(map(float, input().split())))
        for j in range(len(errors[i])):
            trans[i][j] = log(trans[i][j])
    
    for i in range(int(input())):
        string = input().rstrip()
        print(solve(alphabets, errors, trans, string))