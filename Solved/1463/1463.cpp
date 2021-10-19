#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<int> dp;
	int i = 1;
	int N; 
	cin >> N;
	dp = vector<int>(N + 1);
	while (i <= N) {
		if (3 * i <= N) {
			if (dp[3 * i] == 0) {
				dp[3 * i] = dp[i] + 1;
			}
			else {
				dp[3 * i] = min(dp[3 * i], dp[i] + 1);
			}
		
		}
		if (2 * i <= N) {
			if (dp[2 * i] == 0) {
				dp[2 * i] = dp[i] + 1;
			}
			else {
				dp[2 * i] = min(dp[2 * i], dp[i] + 1);
			}
		}
		if (i + 1 <= N) {
			if (dp[i + 1] == 0) {
				dp[i + 1] = dp[i] + 1;
			}
			else {
				dp[i + 1] = min(dp[i + 1], dp[i] + 1);
			}
		}
		i++;
	}
	cout << dp[N];
	return 0;
}
