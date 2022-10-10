#include <stdio.h>
#include <limits.h>
int main()
{
	int a,b,i;
	int max = INT_MIN;
	int min = INT_MAX;
	scanf("%d", &a);
	for(i=0;i<a;i++)
	{
		scanf("%d", &b);
		if(b>max) max = b;
		if(b<min) min = b; 
	}
	printf("%d %d", min,max);
	return 0;
}