#include <iostream>

using namespace std;
int self[10002];

void selfNumber(int a)
{
    if(a>=10000) return ;
    if(a<10) self[a+a] = a+a;
    else if(a<100) self[a+(a/10)+(a%10)] = a+(a/10)+(a%10);
    else if(a<1000) self[a+(a/100)+((a%100)/10)+(a%10)] = a+(a/100)+((a%100)/10)+(a%10);
    else if(a<10000) self[a+(a/1000)+((a%1000)/100)+((a%1000)%100)/10+((a%1000)%100)%10] = a+(a/1000)+((a%1000)/100)+((a%1000)%100)/10+((a%1000)%100)%10;

    selfNumber(a+a);
    selfNumber(a+a+1);
}

int main()
{
    selfNumber(1);
    for(int i=1;i<=10000;i++)
    {
        if(self[i]==0)
        {
            cout<<i<<endl;
        }
    }
    return 0;
}
