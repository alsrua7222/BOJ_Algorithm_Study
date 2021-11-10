from itertools import combinations
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

# 무조건 배워야 하는 글자. a c i n t
# answer에 미리 셋팅해서 무조건 배워야 하는 글자를 뺀 중간 단어가 비어 있을 경우 1씩 더 해준다.
used = set(list("acint"))
answer = 0
arr = []
for _ in range(N):
    tmp = input()[4:-4]
    if tmp:
        set1 = set()
        for v in tmp:
            if v not in used:
                set1.add(v)
        if not set1:
            answer += 1
        else:
            arr.append(set1)
    else:
        answer += 1

# 무조건 배워야 하는 글자 수가 5개.
# K = 5라면 그대로 answer 출력하거나, K <= 4 라면 0을 출력하고 같이 종료한다.
if K <= 5:
    if K == 5:
        print(answer)
    else:
        print(0)
    exit(0)

# 미리 전처리한 arr 원소들 중에 하나라도 포함되어 있지 않는다면 거짓 반환.
# 나머지는 참 반환.
def IsInside(comb, arr_set):
    for v in arr_set:
        if v not in comb:
            return False
    return True

# 조합론으로 모든 경우의 수를 따지면서 푼다.
# 알파벳 순서로 불편하게 작성하지말고 키보드에서 보이는대로 무조건 배워야 하는 단어를 빼고 하나씩 누른다.
alphas = "qweryuopsdfghjklzxvbm"
mid_answer = answer
for comb_elements in combinations(alphas, K):
    comb_elements = set(comb_elements)
    total = mid_answer
    for set_element in arr:
        # 경우의 수 길이가 중단 단어의 길이보다 짧다면 이는 배울 수 없음을 의미함.
        if K < len(set_element):
            continue
        if IsInside(comb_elements, set_element):
            total += 1
    answer = max(answer, total)
print(answer)