#include <stdio.h>
#include <string.h>

int find[26];
char a[1000001];

int main()
{
    int max=0,i,sum=0,size;
    scanf("%s",a);
    size=strlen(a);
    for(i=0;i<size;i++)
    {
        if(a[i] >= 'a')
        {
            find[a[i]-97]++;
        }
        else
        {
             find[a[i]-65]++;
        }
    }
    for(i=0;i<26;i++)
    {
        if(max==find[i])
        {
            sum='?';
        }
        else if(max<find[i])
        {
            max = find[i];
            sum = i+'A';
        }
    }
    printf("%c", sum);
    return 0;
}