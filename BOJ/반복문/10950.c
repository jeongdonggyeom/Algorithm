#include <stdio.h>
int main()
{
	int t,a,b,i,j;
	int sum[100]={0};
	scanf("%d", &t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d", &a,&b);
		sum[i] = a+b;
	}
	for(i=0;i<t;i++)
	{
		printf("%d\n", sum[i]);
	}
}