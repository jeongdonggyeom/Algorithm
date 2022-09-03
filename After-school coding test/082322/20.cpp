#include <iostream>
using namespace std;

int A[101];
int B[101];

int main() {
	int N;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>A[i];
	}
	for(int i=0;i<N;i++){
		cin>>B[i];
	}
	for(int i=0;i<N;i++){
		if(A[i]==1){
			if(B[i]==1) cout<<"D"<<"\n";
			else if(B[i]==2) cout<<"B"<<"\n";
			else if(B[i]==3) cout<<"A"<<"\n";
		}
		else if(A[i]==2){
			if(B[i]==1) cout<<"A"<<"\n";
			else if(B[i]==2) cout<<"D"<<"\n";
			else if(B[i]==3) cout<<"B"<<"\n";
		}
		else if(A[i]==3){
			if(B[i]==1) cout<<"B"<<"\n";
			else if(B[i]==2) cout<<"A"<<"\n";
			else if(B[i]==3) cout<<"D"<<"\n";
		}
	}
	return 0;
}