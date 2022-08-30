#include <iostream>
using namespace std;
int main() {
	char input[100];
	cin >> input;
	int open=0, close=0, last;
	if(input[0] == ')') {
		cout<<"NO";
		return 0;
	}
	for(int i=0;input[i]!=NULL;i++){
		if(input[i] == '(') open+=1;
		if(input[i] == ')') close+=1;
		last = i;
	}
	if(open-close == 0) {
		if(input[last] == '('){
			cout<<"NO";
			return 0;
		}
		cout<<"YES";
	}
	else cout<<"NO";
	return 0;
}