#include <iostream>
using namespace std;

int arr[101];

int main() {
	int N;
	cin>>N;
	int max = ((N*(2 + (N-1)*1))/2)-N;
	for(int i=0;i<N;i++){
		cin>>arr[i];
	}
	for(int i=1;i<N;i++){
		if(arr[i] > arr[i-1]) max = max - (arr[i]-arr[i-1]);
		else max = max - (arr[i-1]-arr[i]);
	}
	if(max==0) cout<<"YES";
	else cout<<"NO";
	return 0;
}