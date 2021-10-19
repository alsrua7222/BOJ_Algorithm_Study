#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int M, N;
	cin >> M; cin >> N;
	vector<bool> dp(N + 1);
	fill(dp.begin(), dp.end(), true);
	dp[0] = dp[1] = false;
	for (int i = 2; i <= sqrt(N); i++) {
		if (dp[i]) {
			for (int j = i + i; j <= N; j += i) {
				dp[j] = false;
			}
		}
	}
	for (int i = M; i <= N; i++) {
		if (dp[i]) {
			cout << i << "\n";
		}
	}
	return 0;
}
