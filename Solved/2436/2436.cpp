#include <iostream>
#include <algorithm>
using namespace std;

int getGCD(int a, int b) {
	if (b == 0) return a;
	else if (a > b) return getGCD(b, a % b);
	else return getGCD(a, b % a);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// gcd = gratest common divisor
	// gcf = greatest common factor
	long gcd, gcf;
	cin >> gcd; cin >> gcf;
	
	int answer[2] = { 0, 0 };
	gcf /= gcd;
	for (int i = 1; i * i <= gcf; i++) {
		if (gcf % i == 0) {
			int a = i, b = gcf / i;
			if (getGCD(a, b) == 1) {
				answer[0] = a; 
				answer[1] = b;
			}
		}
	}
	cout << answer[0] * gcd << " " << answer[1] * gcd;
	return 0;
}
