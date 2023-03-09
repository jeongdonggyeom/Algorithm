#include <iostream>

using namespace std;

int func(int n)
{
    if(n==1 || n==2) return 1;
    return func(n-1) + func(n-2);
}
int main()
{
    int n;
    cin>>n;
    if(n==0) {
        cout<<n;
        return 0;
    }
    int result = func(n);
    cout<<result;
    return 0;
}