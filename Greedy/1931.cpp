#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int, string>a, pair<int, string>b) {
	return a.first < b.first;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int cnt;
	cin >> cnt;
	vector<pair<int, string>> v;
	for (int i = 0; i < cnt; i++) {
		int n;
		string m;
		cin >> n >> m;
		
		v.push_back(make_pair(n, m));
		
	}
	stable_sort(v.begin(), v.end(),compare);
	for (unsigned int i = 0; i < v.size();i++) {
		cout << v.at(i).first << " " << v.at(i).second << '\n';
	}
	return 0;
}