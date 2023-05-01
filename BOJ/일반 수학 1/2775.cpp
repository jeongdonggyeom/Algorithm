#include <iostream>

using namespace std;

int arr[16][16];

void setArray(int a, int b)
{
    for(int i=2;i<=b;i++){
        if(arr[a-1][b] == 0) setArray(a-1, b);
        arr[a][i] = arr[a-1][i] + arr[a][i-1]; 
    }
}

int main()
{
    int T, k, n;
    cin>>T;
    for(int i=1;i<=15;i++){
        arr[0][i] = i;
        arr[i-1][1] = 1;
    }
    for(int i=0;i<T;i++){
        cin>>k>>n;
        if(arr[k][n] != 0){
            cout<<arr[k][n]<<endl;
            continue;
        }
        setArray(k, n);
        cout<<arr[k][n]<<endl;
    }
    return 0;
}