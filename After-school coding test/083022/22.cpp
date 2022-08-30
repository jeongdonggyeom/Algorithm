#include <iostream>
using namespace std;

int arr[100001];

int main() {
	int N,K, sum, max=0;
	cin>>N>>K;
	for(int i=0;i<N;i++){
		cin>>arr[i];
	}
	for(int i=0;i<N;i++){
		sum = 0;
		for(int j=i;j<i+K;j++){
			sum += arr[j];
		}
		if(max < sum) max = sum;
	}
	cout<<max;
	return 0;
}