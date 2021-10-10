# 소수의 연속합
https://www.acmicpc.net/problem/1644
## 해결 과정
### 0. N를 먼저 받아서 아래와 같은 조건을 따른다.
1이면 0으로 출력하고 종료.    
2, 3이면 1으로 출력하고 종료.   
그 외이면, N이 소수인지 따로 구한다.    sqrt(N)으로 판별해서 속도 줄인다.
### 1. N = 4,000,000가 최댓값이므로, 빠르게 에라토스테네스의 체 방법으로 소수 판별을 하면서 리스트를 만든다.
### 2. 소수 배열을 가지고 누적합하면서 N이랑 같으면 카운트 증가하도록 한다.
### 3. 난 투 포인터를 써서 활용했다.
### 4. N 보다 작으면 total에 x 인덱스로 소수 값을 합치고 x에 1씩 증가한다.
### 5. N 보다 크면 total에 y 인덱스로 소수 값을 합치고 y에 1씩 증가한다.
### 6. 그렇게 비교하다보면 카운트가 잘 쌓이고 출력하면 된다.