#include <iostream>
using namespace std;

int a[11];
int b[11];

int main() {
	int winA=0, winB=0;
	for(int i=0;i<2;i++){
		for(int j=0;j<10;j++){
			if(i==0) cin>>a[j];
			else cin>>b[j];
		}
	}	
	for(int i=0;i<10;i++){
		if(a[i] > b[i]) winA+=3;
		else if(a[i] < b[i]) winB+=3;
		else if(a[i] == b[i]) {
			winA+=1;
			winB+=1;
		}
	}
	cout<<winA<<" "<<winB<<"\n";
	if(winA > winB) cout<<"A";
	else if(winA < winB) cout<<"B";
	else if(winA == winB) cout<<"D";
	return 0;
}