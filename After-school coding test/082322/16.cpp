#include <iostream>
#include <algorithm>
using namespace std;
char input[101];
char input2[101];
int main() {
	cin >> input >> input2;
	int cnt=0;
	bool tf=true;
	for(int i=0;input[i]!=NULL;i++){
		cnt++;
	}
	sort(input, input+cnt);
	sort(input2, input2+cnt);
	
	for(int i=0;input[i]!=NULL;i++){
		if(input[i] != input2[i]){
			tf = false;
			break;
		}
	}
	if(tf) cout<<"YES";
	else cout<<"NO";
	return 0;
}