# 가르침
https://www.acmicpc.net/problem/1062
## 해결 과정
### 0. 무조건 배워야 하는 글자 수가 [a, c, i, n, t]이며 총 5개이다. 아래 조건에 따른다.
K가 5이라면 입력받은 것들 중에서 무조건 배워야 하는 글자 수를 뺀 중간 단어만 집계해서 출력한다.        
K가 4개 이하라면 절대 못 배우므로 0 출력한다.        
K가 6개 이상이라면 K에 5개를 빼서 나머지 작업을 한다.       
### 1. 입력단에서 작업 좀 처리한다.
```python
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
```
### 2. 아까 0번에서 기록한 조건들을 구현한다.
```python
# 무조건 배워야 하는 글자 수가 5개.
# K = 5라면 그대로 answer 출력하거나, K <= 4 라면 0을 출력하고 같이 종료한다.
if K <= 5:
    if K == 5:
        print(answer)
    else:
        print(0)
    exit(0)
K -= 5
```
### 3. 조합론으로 모든 경우의 수를 주어진 조건에 따라 처리한다.
```python
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
```
```python
# 미리 전처리한 arr 원소들 중에 하나라도 포함되어 있지 않는다면 거짓 반환.
# 나머지는 참 반환.
def IsInside(comb, arr_set):
    for v in arr_set:
        if v not in comb:
            return False
    return True
```
### 4. 모든 경우의 수를 탐색했다면 answer를 출력한다. 