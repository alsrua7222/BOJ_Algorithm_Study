#include <iostream> // min, max, stdio
#include <algorithm> // sort
#include <vector> // default data struct
#include <cmath> // pow, sqrt, ceil, floor
#include <sstream> // for string
#include <string> // string methods
#include <queue> // queue, priority_queue
#include <deque> // deque
#include <utility> // pair
#include <cstring>
#include <unordered_map> // hash_map (<hash_map> lib is not used, cuz will be delete lib.)
#include <set> // sorted set
#include <map> // sorted map
using namespace std;
#define ll long long

ll getAnswer(ll n) {
	ll answer = n;
	for (ll i = 2; i <= sqrt(n); i++) {
		if (n % i == 0) {
			n /= i;
			while (n % i == 0) {
				n /= i;
			}
			answer *= (1 - (1 / (double)i));
		}
	}
	if (n != 1) answer *= (1 - (1 / (double)n));
	return answer;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	ll n; cin >> n;
	cout << getAnswer(n);
	return 0;
}