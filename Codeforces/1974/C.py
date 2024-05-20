import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    tuple_123 = [{}, {}, {}]
    tuple2_123 = [{}, {}, {}]
    answer = 0

    for i in range(n - 2):
        a1 = (a[i], a[i+1])
        if a1 in tuple_123[0]:
            tuple_123[0][a1] += 1
        else:
            tuple_123[0][a1] = 1
        
        a2 = (a[i+1], a[i+2])
        if a2 in tuple_123[1]:
            tuple_123[1][a2] += 1
        else:
            tuple_123[1][a2] = 1
        
        a3 = (a[i], a[i+2])
        if a3 in tuple_123[2]:
            tuple_123[2][a3] += 1
        else:
            tuple_123[2][a3] = 1
        
        tp = (a[i], a[i+1], a[i+2])
        if tp in tuple2_123[0]:
            tuple2_123[0][tp] += 1
        else:
            tuple2_123[0][tp] = 1
        
        if tp in tuple2_123[1]:
            tuple2_123[1][tp] += 1
        else:
            tuple2_123[1][tp] = 1
        
        if tp in tuple2_123[2]:
            tuple2_123[2][tp] += 1
        else:
            tuple2_123[2][tp] = 1
        
        answer += tuple_123[0][a1] - tuple2_123[0][tp]
        answer += tuple_123[1][a2] - tuple2_123[1][tp]
        answer += tuple_123[2][a3] - tuple2_123[2][tp]

    print(answer)
        