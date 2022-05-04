# 소수 구하기
https://www.acmicpc.net/problem/1929
## 해결 과정
### 0. DP를 이용해서 에라토스테네스 체 기법을 이용해서 푼다.
기존 제곱근 기법으로 풀면 통과가 되나, 시간이 마음 들지 않았다.   
따라서 제곱근 기법으로 푸는 과정 중에 계산했던 것을 또 계산하는 것을 방지하기 위해 DP 적용한다.    
### 1. 출력.