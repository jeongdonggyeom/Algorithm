#include <iostream>

using namespace std;

void func(int a)
{
	int cnt=1;
	for(int i=1;i<=a/2;i++){
		if(a%i==0) cnt++;
	}
	cout<<cnt<<" ";
}

int main() {
	int N;
	cin>>N;
	for(int i=1;i<=N;i++){
		if(i==1){
			cout<<i<<" ";
			continue;
		}
		func(i);	
	}
	return 0;
}