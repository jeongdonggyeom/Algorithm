#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char s[101];
    int find[26];
    int size,i,j;
    cin>>s;
    size = strlen(s);
    fill_n(find, 26, -1);
    for(i=0;i<size;i++)
    {
        for(j=0;j<26;j++)
        {
            if(s[i]==('a'+j) && find[j]==-1)
            {
                find[j] = i;
            }
        }
    }
    for(i=0;i<26;i++)
    {
        printf("%d ", find[i]);
    }
    return 0;
}