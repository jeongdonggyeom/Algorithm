#include <stdio.h>

int main(){
    int c,i,n,j;
    int a[1001];
    double sum=0; 
    double cnt=0;
    double avg[100];
    scanf("%d",&c);
    for(i=0;i<c;i++){
        scanf("%d",&n);
        for(j=0;j<n;j++){
            scanf("%d",&a[j]);
            sum += a[j];
        }
        sum = sum/n;               
        for(j=0;j<n;j++){
            if(a[j]>sum) cnt++;            
        }
        avg[i] = cnt/n*100;       
        cnt=0;
        sum=0;
    }
    for(i=0;i<c;i++){
        printf("%.3lf%\n", avg[i]);
    }
    return 0;
}