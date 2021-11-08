# 음주 코딩
https://www.acmicpc.net/problem/5676
## 해결 과정
### 0. 세그먼트 트리 문제이다.
### 1. 일단, 곱을 해서 양수면 +, 음수면 -, 0이면 0을 출력한다.
이 조건을 만족시키기 위해, 우선 쓸데없는 큰 자료형 곱연산을 방지하기 위해 -1, 0, 1만 사용한다.
### 2. 이는 구간곱 구하는 것이랑 똑같다.
[구간곱 구하기](https://www.acmicpc.net/problem/11505)
### 3. 입력단이 무한이기 때문에 EOF 만날 때까지 하므로, try~catch를 써야 한다.
### 4. 트리의 높이는 (log2(N) + 1)bit 이다. 정수형을 나타내기 위해 ceil를 올려줘야 한다.
### 5. 트리 배열에 사이즈 할당한 후, 작업을 수행한다.
### 6. init 함수 - 구간곱을 나타내기 위해 부모 노드에 자식 노드의 값을 이어받으면서 상태 변경을 한다.
```python
def init(start, end, here):
    if start == end:
        tree[here] = arr[start]
        return tree[here]
    mid = (start + end) // 2
    tree[here] = init(start, mid, here * 2) * init(mid + 1, end, here * 2 + 1)
    return tree[here]
```
### 7. update 함수 - 해당 인덱스의 값이 변경되었다는 신호를 준다.
```python
def update(start, end, here, index, value):
    if index < start or end < index:
        return tree[here]
    if start == end:
        tree[here] = value
        return tree[here]

    mid = (start + end) // 2
    tree[here] = update(start, mid, here * 2, index, value) * update(mid + 1, end, here * 2 + 1, index, value)
    return tree[here]
```
이 때, value값은 -1, 0, 1 중 한 가지만 사용한다.
### 8. query 함수 - 해당 구간의 곱을 반환한다.
```python
def query(start, end, here, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[here]
    mid = (start + end) // 2
    return query(start, mid, here * 2, left, right) * query(mid + 1, end, here * 2 + 1, left, right)
```
### 9. 쿼리들을 받아내면서 변경, 처리를 따로 처리한다.
```python
init(0, N - 1, 1)
answer = ""
for _ in range(M):
    cmd = list(input().split())
    cmd[1:] = map(int, cmd[1:])
    if cmd[0] == 'C':
        if cmd[2] > 0:
            cmd[2] = 1
        elif cmd[2] < 0:
            cmd[2] = -1
        update(0, N - 1, 1, cmd[1] - 1, cmd[2])
    else:
        tmp = query(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)
        answer += "+" if tmp > 0 else '0' if tmp == 0 else '-'
print(answer)
```
출력단에서 변경 쿼리가 들어오면 먼저 변경할 수(-1, 0, 1)를 간단하게 변경하고 업데이트 시행한다.      
처리 쿼리가 들어오면 쿼리 함수를 통해 얻은 값을 양수인지 음수인지 기호를 할당하고, 아니라면 0이므로 0를 할당하여 answer에 적재시킨다.        
출력단에서 끝나면 answer를 출력한다.
