#include <iostream>

using namespace std;
int main() {
	char arr[15], gender;
	cin>>arr;
	if(arr[7] == '1' || arr[7] == '3') gender = 'M';
	else gender = 'W';
	
	if(arr[7] == '1' || arr[7] == '2'){
		cout<<120-((arr[0]-48)*10+(arr[1]-48))<<" "<<gender;
	}
	else{
		cout<<20-((arr[0]-48)*10 + (arr[1]-48))<<" "<<gender;
	}
	return 0;
}