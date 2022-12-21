#include <stdio.h>

int main(){
    int a,b,c;
    int bun=0;
    scanf("%d %d", &a,&b);
    scanf("%d",&c);

    bun = b+c;
    while(bun>=60){
        a+=1;
        bun-=60;
    }
    if(a>=24) a -= 24;
    printf("%d %d", a, bun);
}