#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <queue>
#include <utility>
using namespace std;
int gcd(int a, int b) {
	if (!b) return a;
	else return gcd(b, a % b);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int N, K; cin >> N; cin >> K;
	int tmp = gcd(N, K);
	cout << tmp << "\n" << N * K / tmp;
	return 0;
}
