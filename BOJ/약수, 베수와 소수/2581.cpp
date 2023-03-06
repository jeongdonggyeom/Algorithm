#include <iostream>

using namespace std;

int main()
{
	int N, M, cnt=0, min;
	bool flag;
	cin>>N>>M;
	for(int i=N;i<=M;i++){
		flag = true;
		if(i==1) continue;
		if(i==2 || i==3){
			if(cnt==0) min=i;
			cnt+=i;
			continue;
		}
		else {
			for(int j=2;j<i;j++){
				if(i%j==0){
					flag = false;
					break;
				}
			}
			if(!flag) continue;
		}
		if(cnt==0) min=i;
		cnt+=i;
	}
	if(cnt==0) cout<<"-1";
	else { 
		cout<<cnt<<endl; 
		cout<<min; 
	}
	return 0;
}
