#include <iostream>
#include <algorithm>
using namespace std;

int arr[101];
int ranking[101];

bool comp(int a, int b){
	return a > b;
}

int main()
{
	int N, cr=1;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>arr[i];
	}
	copy(arr, arr+N, ranking);
	sort(arr, arr+N, comp);
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(arr[i] == ranking[j]) ranking[j] = cr; 
		}
		cr++;
	}
	
	for(int i=0;i<N;i++){
		cout<<ranking[i]<<" ";
	}
	return 0;
}