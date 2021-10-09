# LCS
https://www.acmicpc.net/problem/9251
## 해결 과정
### 0. DP 2차원으로 풀어야 한다.
예를 들어,  
str1 = ACAYKP   
str2 = CAPCAK   
라고 했을 경우,
DP[len(str2) + 1][len(str1)]로 선언하고, 첫번째 인덱스를 초기화 시킨다.   
str2[0] = C 라고 가정하면.
i는 반복문으로 1씩 증가한다고 치면, dp[0][i] = 0 저장하다가 str2[0] == str1[i] 되는 순간부터 dp[0][i] = 1 저장해준다.
마찬가지 반대도 똑같다.
### 1. 2번째 인덱스 라인부터 스타트한다. 단, 아래 조건을 만족하면서 반복한다.
증가 연산자가 i, j가 있다면 for i => for j 에서   
if str2[i] == str2[j] 이라면 dp[i][j] = dp[i - 1][j - 1] + 1.    
else str2[i] != str2[j] 이라면 dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])로 저장한다.
### 2. dp의 마지막 원소 위치를 불러오면 그게 가장 큰 길이로 불러온다.
