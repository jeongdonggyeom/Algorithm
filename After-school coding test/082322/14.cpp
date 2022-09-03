#include <iostream>
#include <cmath>
using namespace std;

int save[1001];
int arr[100001];

void Eratos()
{
  fill_n(arr+2, 100000, true); // 처음에 배열을 모두 true로 초기화해줌.
    for(int i=2;i<=100000;i++){ // 2부터 시작
        for(int j=i*2;j<=100000;j+=i){ // i의 배수
            arr[j]=false;   // 걸러내는 작업
        }
    }
}

int main() {
	int N, a, newNum, cnt;
	cin>>N;
	Eratos();
	for(int i=0;i<N;i++){
		cin>>a;
		newNum = 0;
		cnt=0;
		while(a>0){
			save[cnt] = a%10;
			a/=10;
			cnt+=1;
		}
		for(int i=cnt;i>0;i--){
			newNum += save[cnt-i]*pow(10, i-1);
		}
		if(arr[newNum]) cout<<newNum<<" ";
	}
	return 0;
}