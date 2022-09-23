from math import ceil
def convTS(ts):
    h, m = ts.split(':')
    return int(h) * 60 + int(m)
    
def solution(fees, records):
    answer = []
    cars_cost = {}
    tot_times = {}
    preIn = {}
    numbers = set()
    for record in records:
        ts, number, state = record.split()
        numbers.add(number)
        if state[0] == "I":
            preIn[number] = convTS(ts)
        else:
            if number in tot_times:
                tot_times[number] += (convTS(ts) - preIn[number])
            else:
                tot_times[number] = (convTS(ts) - preIn[number])
            preIn[number] = -1
    
    for key, value in preIn.items():
        if value == -1:
            continue
        
        if key in tot_times:
            tot_times[key] += (convTS("23:59") - preIn[key])
        else:
            tot_times[key] = (convTS("23:59") - preIn[key])
        preIn[key] = 0
    
    for key in sorted(numbers):
        answer.append(fees[1])
        if fees[0] < tot_times[key]:
            answer[-1] += ceil((tot_times[key] - fees[0]) / fees[2]) * fees[3]
            
    return answer