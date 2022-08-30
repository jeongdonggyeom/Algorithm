#include <iostream>
using namespace std;
int main() {
	int A, B, sum=0;
	cin>>A>>B;
	cout<<A<<" ";
	sum+=A;
	for(int i=A+1; i<=B;i++){
		cout<<"+ "<<i<<" ";
		sum += i;
	}
	cout<<"= "<<sum;
	return 0;
}