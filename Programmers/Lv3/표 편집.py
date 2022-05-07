def solution(n, k, cmd):
    answer = ''
    
    linked_list = {}
    for i in range(n):
        if i == 0:
            linked_list[i] = [None, i + 1]
        elif i == n - 1:
            linked_list[i] = [i - 1, None]
        else:
            linked_list[i] = [i - 1, i + 1]
    
    total = 0
    garbage = []
    for query in cmd:
        if len(query) == 1:
            if total < 0:
                for i in range(-total):
                    k = linked_list[k][0]
            else:
                for i in range(total):
                    k = linked_list[k][1]
            total = 0

            if query == 'C':
                garbage.append(k)
                if linked_list[k][1] is None:
                    linked_list[linked_list[k][0]][1] = None
                    k = linked_list[k][0]
                elif linked_list[k][0] is None:
                    linked_list[linked_list[k][1]][0] = None
                    k = linked_list[k][1]
                else:
                    linked_list[linked_list[k][0]][1] = linked_list[k][1]
                    linked_list[linked_list[k][1]][0] = linked_list[k][0]
                    k = linked_list[k][1]
            else:
                point = garbage.pop()
                if linked_list[point][0] is not None:
                    linked_list[linked_list[point][0]][1] = point
                if linked_list[point][1] is not None:
                    linked_list[linked_list[point][1]][0] = point
        else:
            query = query.split()
            command = query[0]
            number = int(query[1])
            if command == 'U':
                total -= number
            else:
                total += number
    
    garbage = set(garbage)
    answer = ''.join('X' if i in garbage else 'O' for i in range(n))
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))