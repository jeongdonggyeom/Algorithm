#include <iostream>
using namespace std;
int main() {
	int N, min=101, max=0, input;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>input;
		if(max < input) max = input;
		if(min > input) min = input;
	}
	cout<<max-min;
	return 0;
}