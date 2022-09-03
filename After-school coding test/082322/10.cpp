#include <iostream>
#include <algorithm>
using namespace std;

int arr[1001];
int save[1001];
int arr2[1001];

bool comp(int a, int b){
	return a > b;
}

int main() {
	int N, a;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>a;
		save[i] = a;
		while(a>0){
			arr[i] += a%10;
			arr2[i] += a%10;
			a/=10;
		}
	}
	sort(arr2, arr2+N, comp);
	for(int i=0;i<N;i++){
		if(arr2[0] != arr[i]) save[i] = 0;
 	}
	sort(save, save+N, comp);
	cout<<save[0];
	return 0;
}