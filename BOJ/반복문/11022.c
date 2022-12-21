#include <stdio.h>
int main()
{
	int t,a,b,i,c[10000]={0};
	int sum[100]={0}, cnt[100]={0};
	scanf("%d", &t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d", &a,&b);
		sum[i] = a;
		cnt[i] = b;
		c[i] = a+b;
	}
	for(i=1;i<=t;i++)
	{
		printf("Case #%d: %d + %d = %d\n",i,sum[i-1],cnt[i-1],c[i-1]);
	}
}