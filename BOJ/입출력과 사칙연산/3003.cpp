#include <iostream>

using namespace std;

int main()
{
	int arr[6], a;
	for(int i=0;i<6;i++){
		cin>>a;
		if(i==0 || i==1){
			arr[i] = 1-a;
		}
		if(i==2 || i==3 || i==4){
			arr[i] = 2-a;
		}
		if(i==5){
			arr[i] = 8-a;
		}
	}
	for(int i=0;i<6;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}