#include <iostream>
using namespace std;

int arr[100001];

int main() {
	int N, last=0, max=0, cnt=1;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>arr[i];
	}
	for(int i=1;i<N;i++){
		if(arr[i] >= arr[last]) cnt+=1;
		else{
			if(cnt>max) max = cnt;
			cnt=1;
		}
		last = i;
	}
	cout<<max;
	return 0;
}