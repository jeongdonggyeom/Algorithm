#include <iostream>
using namespace std;
int arr[1001];
int main() {
	int N, a=0;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>arr[i];
	}
	int max = arr[N-1];
	for(int i=N-2;i>0;i--){
		if(arr[i] > max){
			max = arr[i];
			a++;
		}
	}
	cout<<a;
	return 0;
}