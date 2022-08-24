#include <iostream>

using namespace std;

int main()
{
	int N, sum=0, cnt=1;
	cin>>N;
	while(true){
		if(N-6*cnt>0){
			N-=6*cnt;
			cnt+=1;
		}
		else break;
	}
	if(N>=2) cout<<cnt+1;
	else cout<<cnt;
	return 0;
}
