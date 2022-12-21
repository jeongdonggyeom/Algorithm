#include <stdio.h>
int main()
{
	int t,i,n,c,a[10000000]={0};
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d", &n,&c);
		a[i] = n+c;
	}
	for(i=0;i<t;i++)
	{
		printf("%d\n", a[i]);
	}
}