#include <stdio.h>
int main()
{
	int N;
	int result;
	int A,B,C,D;
	int cnt=0;
	
	scanf("%d",&N);
	result = N;
	
	while(1)
	{
		A = N/10;
		B = N%10;
		C = (A+B)%10;
		D = (B*10) + C;
		N = D;
		cnt++;
		if(D==result) break;
	}
	printf("%d",cnt);
}