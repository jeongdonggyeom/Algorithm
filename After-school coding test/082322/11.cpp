#include <iostream>

using namespace std;

int main()
{
	int N, result=0;
	cin>>N;
	for(int i=1;i<=N;i++){
		if(i<10) result+=1;
		else if(i<100) result+=2;
		else if(i<1000) result+=3;
		else if(i<10000) result+=4;
		else if(i<100000) result+=5;
	}
	cout<<result;
}