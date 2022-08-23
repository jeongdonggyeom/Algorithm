#include <iostream>

using namespace std;

int main()
{
	int N, i=2;
	cin>>N;
	if(N==1) return 0;
	while(N>1){
		if(N%i==0){
			N = N/i;
			cout<<i<<endl;
			continue;
		}
		i+=1;
	}

	return 0;
}
