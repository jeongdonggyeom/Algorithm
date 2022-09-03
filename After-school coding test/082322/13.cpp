#include <iostream>

using namespace std;
char input[101];
int num[10];

int main() {
	int index, max=0;
	cin>>input;
	for(int i=0;input[i]!=NULL;i++){
		num[input[i]-48]++;
	}
	for(int i=0;i<10;i++){
		if(num[i] > max){
			max = num[i];
			index = i;
		}
		if(num[i] == max){
			index = i;
		}
	}
	cout<<index;
	return 0;
}