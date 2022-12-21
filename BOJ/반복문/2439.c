#include <stdio.h>
int main()
{
	int a,i,j;
	scanf("%d", &a);
	for(i=0;i<a;i++)
	{
		for(j=i;j<a-1;j++)
		{
			printf(" ");
		}
		for(j=0;j<=i;j++)
		{
			printf("*");
		}
		printf("\n");
	}
}