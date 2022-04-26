#include <iostream> // min, max, stdio
#include <algorithm> // sort
#include <vector> // default data struct
#include <cmath> // pow, sqrt, ceil, floor
#include <sstream> // for string
#include <string> // string methods
#include <queue> // queue, priority_queue
#include <deque> // deque
#include <utility> // pair
#include <unordered_map> // hash_map (<hash_map> lib is not used, cuz will be delete lib.)
using namespace std;
int N, M, V;
unordered_map<int, vector<int>> Graph;
vector<bool> visited;

void DFS(int start) {
	cout << start << " ";
	for (int i = 0; i < Graph[start].size(); i++) {
		if (visited[Graph[start][i]]) continue;
		visited[Graph[start][i]] = true;
		DFS(Graph[start][i]);
	}
	return;
}

void BFS(int start) {
	int node;
	queue<int> Queue;
	Queue.push(start);
	while (!Queue.empty()) {
		node = Queue.front();
		Queue.pop();
		cout << node << " ";
		for (int i = 0; i < Graph[node].size(); i++) {
			if (visited[Graph[node][i]]) continue;
			visited[Graph[node][i]] = true;
			Queue.push(Graph[node][i]);
		}
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++) {
		int s, e; cin >> s >> e;
		Graph[s].push_back(e);
		Graph[e].push_back(s);
	}
	for (int i = 1; i <= N; i++) {
		sort(Graph[i].begin(), Graph[i].end());
	}
	visited.assign(N + 1, false);
	visited[V] = true;
	DFS(V);
	
	cout << "\n";
	visited.assign(N + 1, false);
	visited[V] = true;
	BFS(V);
	return 0;
}
