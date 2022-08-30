#include <iostream>

using namespace std;

char input[101];

int main() {
	for(int i=0;i<100;i++){
		cin>>input[i];
		if(input[i] != NULL){
			if(input[i] >= 65 && input[i] <= 90){
				cout<<static_cast<char>(input[i]+32);
			}
			else cout<<static_cast<char>(input[i]);
		}
	}
	return 0;
}