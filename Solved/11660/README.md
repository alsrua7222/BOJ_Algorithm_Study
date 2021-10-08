# 구간 합 구하기 5
https://www.acmicpc.net/problem/11660
## 해결 과정
### 0. DP로 누적합을 시키면 된다.
### 1. 1번째 라인(열, 행)은 간단히 arr 배열과 dp 배열을 합치면서 저장시킨다.
### 2. 2번쨰 라인(열, 행) 이상은 dp[col][row] = dp[col - 1][row] + dp[col][row - 1] - dp[col - 1][rpw -1] + arr[col - 1][row - 1]로 맞춘다.
arr[col - 1][row - 1]인 이유는 dp 배열에 1번째 인덱스가 아닌 0번째 인덱스(벗어난 범위)에 0으로 확장되어 있기 때문.    
### 3. 메모이제이션 끝나면 쿼리를 통해서 간단히 dp 불러오면 된다.
### 4. dp[y2][x2] - dp[y1 - 1][x2] - dp[y2][x1 - 1] + dp[y1 - 1][x1 - 1]

[Image](https://github.com/alsrua7222/BOJ_Algorithm_Study/blob/main/Solved/11660/snap.PNG)
