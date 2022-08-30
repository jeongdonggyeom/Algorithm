#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
int main() {
	char input[51];
	vector<int> v;
	int num=0, cnt=-1, sum=0;
	cin >> input;
	
	for(int i=0;input[i]!=NULL;i++){
		if(input[i] >= 48 && input[i] <= 57){
			v.push_back(input[i]-48);
			cnt++;
		}
	}
	
	for(int i=0;i<v.size();i++){
		num+=v[i] * pow(10, cnt);
		cnt--;
	}
	for(int i=1;i<=num;i++){
		if(num%i==0) sum++;
	}
	cout<<num<<"\n";
	cout<<sum;
	
	return 0;
}