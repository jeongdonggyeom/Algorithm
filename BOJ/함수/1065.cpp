#include <iostream>

using namespace std;

int main()
{
    int n,f,m,l,cnt=0;
    cin>>n;
    if(n<100)
    {
        cout<<n;
        return 0;
    }
    else
    {
        for(int i=100;i<=n;i++)
        {
            f = i/100;
            m = (i%100)/10;
            l = (i%100)%10;
            if(f-m == m-l) cnt++;
        }
    }
    cout<<cnt+99;
    return 0;
}
