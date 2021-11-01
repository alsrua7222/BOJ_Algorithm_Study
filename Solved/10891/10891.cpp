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
#include <stack> // stack
using namespace std;
unordered_map<int, vector<int>> Graph;
vector<int> visited, parents;
int N, M;
bool DFS(int cur) {
	visited[cur]++;
	for (int next : Graph[cur]) {
		if (next == parents[cur] || visited[next] == 2) continue;
		if (visited[next] == 0) {
			parents[next] = cur;
			if (!DFS(next)) return false;
		}
		else {
			int tmp = cur;
			while (tmp != parents[next]) {
				if (visited[tmp] == 2) return false;
				visited[tmp]++;
				tmp = parents[tmp];
			}
		}
	}
	return true;
}
	
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> N >> M;
	visited.assign(N + 1, 0);
	parents.assign(N + 1, 0);
	for (int i = 0; i < M; i++) {
		int u, v;
		cin >> u >> v;
		Graph[u].push_back(v);
		Graph[v].push_back(u);
	}

	if (DFS(1)) cout << "Cactus";
	else cout << "Not cactus";

	return 0;
}