#include <stdio.h>

int main(){
    int a[3],i,max=0;
    scanf("%d %d %d", &a[0],&a[1],&a[2]);
    if(a[0]==a[1] && a[1]==a[2]){
        printf("%d", 10000+a[1]*1000);
    }
    else if(a[0]==a[1]){
        if(a[1]!=a[2]){
            printf("%d",1000+a[0]*100);
        }
    }
    else if(a[1]==a[2]){
        if(a[0]!=a[1]){
            printf("%d",1000+a[1]*100);
        }
    }
    else if(a[0]==a[2]){
        if(a[1]!=a[2]){
            printf("%d",1000+a[2]*100);
        }
    }
    else{
        for(i=0;i<3;i++){
            if(max<a[i]) max=a[i];
        }
        printf("%d",max*100);
    }
}