#include <stdio.h>

long long sum(int *a, int n) {
	long long ans = 0;
    int i;
    for(i=0;i<n;i++)
    {
        ans = ans+a[i];
    }
	return ans;
}
int akdoapd(){
    int n,i,q=0;
    int a[1000000]={0,};
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    q=sum(a,n);
    printf("%d",q);
    return 0;
}