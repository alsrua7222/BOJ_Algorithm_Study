# 버블 소트
https://www.acmicpc.net/problem/1377
## 해결 과정
### 0. 이 문제를 요약하자면 버블 소트 몇번 시행했는지 출력하는 것이다.
### 1. 그대로 버블 소트로 풀면 시간초과로 터진다.
### 2. 그래서 인덱스 거리로 인덱스를 줄여나가면서 확인해 보는 방법으로 해야 한다.
### 3. 소트 방법은 O(N^2)가 아닌 O(NlogN)인 퀵+병합 정렬로 푼다.(python sort 이용).
### 4. 정렬된 배열과 정렬 안된 배열을 비교하면서 인덱스 거리르 측정한다.
### 5. 인덱스 거리는 곧 해당 원소의 버블소트의 최대 횟수를 알 수 있다.
```python
for i in range(N):
    if after[i][1] > i:
        answer = max(answer, abs(after[i][1] - i))
```
소트하기 전에 저장한 인덱스 정보를 가지고 현재 인덱스보다 높아야 한다. 그러면 버블소트 횟수를 정확하게 알 수 있다.      
### 6. answer 출력한다.