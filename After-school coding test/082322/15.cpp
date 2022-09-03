#include <iostream>
using namespace std;

int arr[200001];

void Eratos(int n)
{
  fill_n(arr+2, n, true); // 처음에 배열을 모두 true로 초기화해줌.
    for(int i=2;i<=n;i++){ // 2부터 시작
        for(int j=i*2;j<=n;j+=i){ // i의 배수
            arr[j]=false;   // 걸러내는 작업
        }
    }
}

int main() {
	int N, cnt=0;
	cin>>N;
	Eratos(N);
	for(int i=2;i<=N;i++){
		if(arr[i]) cnt++;
	}
	cout<<cnt;
	return 0;
}