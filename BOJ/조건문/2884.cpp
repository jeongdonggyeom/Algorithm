#include <stdio.h>
int main()
{
	int a,b;
	scanf("%d %d", &a,&b);
	if(b<45)
	{
		b+=60;
		b-=45;
		if(a==0)
		{
			a=24;
			a-=1;
			printf("%d %d", a,b);
			return 0;
		}
		printf("%d %d", a-1,b);
		return 0;
	}
    printf("%d %d", a,b-45);
}