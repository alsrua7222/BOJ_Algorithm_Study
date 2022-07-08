from math import log
import sys
input = sys.stdin.readline
class Results:
    def __init__(self, char):
        self.prefix = ""
        self.prior = 0
        self.myChar = char
        self.ProbIndex = -float('inf')
        return
    def process(self):
        self.prefix += self.myChar
        self.prior += self.ProbIndex
        self.ProbIndex = -float('inf')
        return

def solve(alphabets: list, errors: list, trans: list, message: str) -> int:
    result = dict()
    
    recvIndex = alphabets.index(message[0])
    for i in range(len(alphabets)):
        curChar = alphabets[i]
        tmpResult = Results(curChar)
        tmpResult.ProbIndex = errors[i][recvIndex]

        result[curChar] = tmpResult
    
    MAX = 1e9 + 1
    
    for i in range(1, len(message)):
        recvIndex = alphabets.index(message[i])

        postResult = dict()
        for r in result.values():
            r.process()
            preIndex = alphabets.index(r.myChar)
            
            for transIndex in range(len(alphabets)):
                sponChar = alphabets[transIndex]
                total = trans[preIndex][transIndex] + errors[transIndex][recvIndex]

                if sponChar in postResult:
                    tmpResult = postResult[sponChar]
                else:
                    tmpResult = Results(sponChar)
                    tmpResult.prefix += r.prefix
                    tmpResult.prior += r.prior
                    postResult[sponChar] = tmpResult
                
                far = tmpResult.prior + tmpResult.ProbIndex
                tot_ability = r.prior + total
                
                if far < tot_ability:
                    if tot_ability - far < MAX:
                        MAX = tot_ability - far
                    
                    tmpResult.ProbIndex = tot_ability
                    tmpResult.prefix = r.prefix
                    tmpResult.prior = r.prior
                    postResult[sponChar] = tmpResult
        result = postResult
    
    answer = ""
    MAX = -float('inf')
    for r in result.values():
        r.process()
        
        if r.prior > MAX:
            MAX = r.prior
            answer = r.prefix
    return answer
    
for _ in range(int(input())):
    ac = int(input())
    alphabets = list(input().split())

    errors = []
    for _ in range(ac):
        tmp = list(map(float, input().split()))
        errors.append(list(map(log, tmp)))
    
    trans = []
    for _ in range(ac):
        tmp = list(map(float, input().split()))
        trans.append(list(map(log, tmp)))
    
    for i in range(int(input())):
        message = input().rstrip()
        print(solve(alphabets, errors, trans, message))