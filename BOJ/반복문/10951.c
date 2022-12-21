#include <stdio.h>
int main()
{
	int a,b,c[100]={0},cnt=0,qwe=0;
	while(scanf("%d %d", &a,&b) != EOF)
	{
		c[cnt++] = a+b;
	}
	c[cnt] = '\0';
	while(c[qwe]!='\0')
	{
		printf("%d\n", c[qwe++]);
	}
	return 0;
}