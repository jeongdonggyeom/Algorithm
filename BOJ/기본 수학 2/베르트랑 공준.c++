#include <iostream>

using namespace std;

int arr[300000];

int main()
{
    int n, cnt=0;
    fill_n(arr+2, 300000, true);
    while(true){
        cnt=0;
        cin>>n;
        if(n==0) break;
        for(int i=2;i<=n*2;i++){
            if(!arr[i]) continue;
           for(int j=i*2;j<=n*2;j+=i){
                arr[j]=false;
            }
        }
        for(int i=n;i<=n*2;i++){
            if(arr[i] && i>n) cnt++; 
        }
        cout<<cnt<<"\n";
    }

    return 0;
}