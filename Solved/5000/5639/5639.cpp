#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
typedef long long ll;
using namespace std;
struct node {
	node* left;
	int mid;
	node* right;
};
void push(int value, node* root) {
	if (root->mid == NULL) {
		root->mid = value;
	}
	else {
		if (root->mid > value) {
			if (root->left == NULL) {
				root->left = (node*)malloc(sizeof(node));

				root->left->left = NULL;
				root->left->right = NULL;
				root->left->mid = NULL;
			}
			push(value, root->left);
		}
		else{
			if (root->right == NULL) {
				root->right = (node*)malloc(sizeof(node));
				root->right->left = NULL;
				root->right->right = NULL;
				root->right->mid = NULL;
			}
			push(value, root->right);
		}
	}
}
void post_order(node* root) {
	if(root->left != NULL){
		post_order(root->left);
	}
	if (root->right != NULL) {
		post_order(root->right);
	}
	cout << root->mid << "\n";
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	node root = { NULL, NULL, NULL };
	int tmp;
	int cnt = 0;
	while (cnt < 10001) {
		if (scanf(" %d", &tmp) == EOF) {
			break;
		}
		push(tmp, &root);
		cnt += 1;
	}
	post_order(&root);
		
}
