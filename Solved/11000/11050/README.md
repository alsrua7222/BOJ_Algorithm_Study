# 이항 계수 1
https://www.acmicpc.net/problem/11050
## 해결 과정
### 0. 분모에 N부터 N - K + 1만큼 누적곱을 하면 된다.
N * (N - 1) * ... * (N - K + 1)
### 1. 분자에 1부터 K만큼 누적곱을 하면 된다.
### 2. 분모 / 분자 하면 값 나온다.
