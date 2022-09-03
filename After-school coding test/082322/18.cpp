#include <iostream>
using namespace std;

int arr[1000];

int main() {
	int N, M, c=0, max=0;
	cin>>N>>M;
	for(int i=0;i<N;i++){
		cin>>arr[i];
	}
	for(int i=0;i<N;i++){
		if(arr[i]>M){
			c++;
		}
		else{
			if(max<c) max = c;
			c=0;
		}
	}
	if(max==0) cout<<"-1";
	else{
		if(c>max) cout<<c;
		else cout<<max;
	}
	return 0;
}