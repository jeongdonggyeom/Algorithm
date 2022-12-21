#include <iostream>

using namespace std;

int main()
{
	int N, a, b, X, sum=0;
	cin>>X;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>a>>b;
		sum += a*b;
	}
	if(X==sum) cout<<"Yes";
	else cout<<"No";
	return 0;
}