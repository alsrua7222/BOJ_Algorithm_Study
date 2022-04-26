# 수열과 쿼리16
https://www.acmicpc.net/problem/14428
## 해결 과정
### 0. 부분 구간에 대한 데이터 내용을 추출하고, 크기가 크기 때문에 세그먼트 트리를 이용해야 한다.
### 1. 트리의 높이는 log 2에 N의 올림한 값이랑 같다.
### 2. 트리는 값을 비교할 트리랑 최소 값의 인덱스를 기억하는 트리면 된다.
### 3. 초기 셋팅할 때, start와 end이 같으면 tree의 현재 상태에 입력 배열[start]를 넣어서 추가하고, 인덱스를 추가한다.
```python
def init(start, end, here):
    if start == end:
        tree[here] = arr[start]
        tree_index[here] = start
        return [tree[here], tree_index[here]]
```
### 4. 그리고 반환할 때, [tree[here], tree_index[here]]를 반환해준다
### 5. 또, 상위(부모) 구간에 대해서 하위(자식) 구간끼리 비교해서 최소한 값과 그에 맞는 인덱스를 저장해야 하므로 아래와 같이 한다.
```python
def init(start, end, here):
    if start == end:
        tree[here] = arr[start]
        tree_index[here] = start
        return [tree[here], tree_index[here]]
    mid = (start + end) // 2
    tmp1 = init(start, mid, here * 2)
    tmp2 = init(mid + 1, end, here * 2 + 1)
    if tmp1[0] < tmp2[0]:
        tree[here] = tmp1[0]
        tree_index[here] = tmp1[1]
    elif tmp1[0] > tmp2[0]:
        tree[here] = tmp2[0]
        tree_index[here] = tmp2[1]
    else:
        if tmp1[1] < tmp2[1]:
            tree[here] = tmp1[0]
            tree_index[here] = tmp1[1]
        else:
            tree[here] = tmp2[0]
            tree_index[here] = tmp2[1]
    return [tree[here], tree_index[here]]
```
본 문제에서는 값이 같다면, 인덱스를 작은 것부터 출력하라고 했으니 이에 맞게 설정해준다.
### 6. 구간 업데이트를 시켜야 하므로, 역시 5번과 비슷한 원리로 자식 노드끼리 비교해서 작은 값을 넣도록 해야 한다.
```python
def update(start, end, here, index, value):
    if end < index or index < start:
        # 자식 노드랑 비교해서 부모 노드로 옮겨줘야 하는 작업 필요.
        return [tree[here], tree_index[here]]
    if index <= start and end <= index:
        tree[here] = value
        return [tree[here], tree_index[here]]
    mid = (start + end) // 2
    tmp1 = update(start, mid, here * 2, index, value)
    tmp2 = update(mid + 1, end, here * 2 + 1, index, value)
    if tmp1[0] < tmp2[0]:
        tree[here] = tmp1[0]
        tree_index[here] = tmp1[1]
    elif tmp1[0] > tmp2[0]:
        tree[here] = tmp2[0]
        tree_index[here] = tmp2[1]
    else:
        if tmp1[1] < tmp2[1]:
            tree[here] = tmp1[0]
            tree_index[here] = tmp1[1]
        else:
            tree[here] = tmp2[0]
            tree_index[here] = tmp2[1]
    return [tree[here], tree_index[here]]
```
이렇게 하면 상위 구간에 하위 구간끼리 비교해서 더 작은 값으로 저장시키는 것이다.      
### 7. 출력해야 하므로 쿼리를 작성하고 편하게 출력하면 된다.
편하게 출력하는 이유는 이미 업데이트하는 과정에서 최소한 값을 다 맞추었기 때문이다.     
그러므로 해당 구간에 포함되면 값을 가져오고 아니라면, 가짜 값을 가져오도록 하면 된다.       
```python
def query(start, end, here, left, right):
    if left > end or right < start:
        # 필요 없는 노드 쪽은 대충 반환.
        return [1234567890, -1]
    if left <= start and end <= right:
        return [tree[here], tree_index[here]]
    mid = (start + end) // 2
    tmp1 = query(start, mid, here * 2 , left, right)
    tmp2 = query(mid + 1, end, here * 2 + 1, left, right)
    if tmp1[0] < tmp2[0]:
        return tmp1
    elif tmp1[0] > tmp2[0]:
        return tmp2
    else:
        if tmp1[1] < tmp2[1]:
            return tmp1
        else:
            return tmp2
```
### 8. 이제 모든 함수를 가지고 쿼리에 맞게 출력한다.
```python
# 값, 인덱스 트리 셋팅.
init(0, N - 1, 1)

M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        update(0, N - 1, 1, cmd[1] - 1, cmd[2])
    else:
        print(query(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)[1] + 1)
```
