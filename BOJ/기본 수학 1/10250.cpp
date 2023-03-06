#include <iostream>

using namespace std;
int main()
{
    int a,height,width;
    int H,N,W;
    cin>>a;
    for(int i=0;i<a;i++)
    {
        cin>>H>>W>>N;
        height = 0;
        width = 1;
        for(int j=0;j<N;j++)
        {
            if(height==H)
            {
                height=1;
                width++;
            }
            else height++;
        }
        if(width<10) cout<<height<<0<<width<<endl;
        else cout<<height<<width<<endl;
    }
}