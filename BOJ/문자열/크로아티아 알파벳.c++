#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char a[101];
    cin>>a;
    int size = strlen(a);
    int cnt = strlen(a);
    for(int i=0;i<cnt;i++)
    {
        if(a[i] == '=')
        {
            if(a[i-1] == 's') size--;
            if(a[i-1] == 'c') size--;
            if(a[i-1] == 'z')
            {
                size--;
                if(a[i-2] == 'd') size--;
            }
        }
        if(a[i] == '-')
        {
            if(a[i-1] == 'c') size--;
            if(a[i-1] == 'd') size--;
        }
        if(a[i] == 'j')
        {
            if(a[i-1] == 'l') size--;
            if(a[i-1] == 'n') size--;
        }
    }   
    cout<<size;
    return 0;
}