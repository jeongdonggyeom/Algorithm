#include <iostream>

using namespace std;

bool arr[1000001];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
    int M, N;
    cin>>M>>N;
    fill_n(arr+2, N, true);
    for(int i=2;i<=N;i++){
        for(int j=i*2;j<=N;j+=i){
            arr[j]=false;
        }
    }
    for(int i=M;i<=N;i++){
        if(arr[i]) cout<<i<<"\n";
    }
}