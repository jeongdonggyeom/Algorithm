#include <iostream>

using namespace std;

int main()
{
	int N, cnt=0;
	cin>>N;
	while(N>2){
		cnt+=1;
		if(N%5==0) N-=5;
		else if(N%3==0) N-=3;
		else if(N>5) N-=5;
		else N-=3;
	}
	if(N==1 || N==2) cout<<"-1";
	else cout<<cnt;

	return 0;
}
