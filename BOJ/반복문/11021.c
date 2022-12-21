#include <stdio.h>
int main()
{
	int t,a,b,i,c[10000]={0};
	scanf("%d", &t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d", &a,&b);
		c[i] = a+b;
	}
	for(i=1;i<=t;i++)
	{
		printf("Case #%d: %d\n",i,c[i-1]);
	}
}