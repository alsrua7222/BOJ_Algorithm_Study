def solution(id_list, report, k):
    answer = []
    cnt_dict = {}
    report_cnt_dict = {}
    report_dict = {}
    used_dict = {}
    # initialize
    for id in id_list:
        cnt_dict[id] = 0
        report_cnt_dict[id] = 0
        report_dict[id] = []
        used_dict[id] = set()
        
    for string in report:
        u, v = string.split()
        if v in used_dict[u]:
            continue
        report_cnt_dict[v] += 1
        report_dict[v].append(u)
        used_dict[u].add(v)
        
    for key, values in report_dict.items():
        if report_cnt_dict[key] >= k:
            for value in values:
                cnt_dict[value] += 1
    
    for id in id_list:
        answer.append(cnt_dict[id])
        
    return answer