#include <stdio.h>
int main()
{
	int a=1,b=1,c[100]={0},cnt=0,sum=0;
	while(a!=0 && b!=0)
	{
		scanf("%d %d", &a,&b);
		c[cnt++] = a+b;
	}
	c[cnt] = '\0';
	while(c[sum]!='\0')
	{
		printf("%d\n",c[sum++]);
	}
}