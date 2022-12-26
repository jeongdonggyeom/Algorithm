#include <stdio.h>
#include <string.h>
int main()
{
	char txt[1000001];
	int i,cnt=0;
	int len;
	scanf("%[^\n]", txt);
	len = strlen(txt);
	if(len == 1)
	{
		if(txt[0] == ' ')
		{
			printf("0\n");
			return 0;
		}
	}
	for(i=1;i<len-1;i++)
	{
		if(txt[i] == ' ') cnt++;
	}
	printf("%d",cnt+1);
	return 0;
}