#include <iostream>
using namespace std;
int main() {
	int N, q, a;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>q>>a;
		if(a == (q*(1+q))/2) cout<<"YES"<<"\n";
		else cout<<"NO"<<"\n";
	}
	return 0;
}