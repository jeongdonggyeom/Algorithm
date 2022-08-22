#include <iostream>

using namespace std;

int main()
{
	int n, a, cnt=0;
	bool flag;
	cin>>n;
	for(int i=0;i<n;i++){
		flag = true;
		cin>>a;
		if(a==1) continue;
		if(a==2 || a==3){
			cnt+=1;
			continue;
		}
		else {
			for(int j=2;j<a;j++){
				if(a%j==0){
					flag = false;
					break;
				}
			}
			if(!flag) continue;
		}
		cnt+=1;
	}
	cout<<cnt;
	return 0;
}
