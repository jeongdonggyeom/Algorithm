#include <stdio.h>
char swap();
char a[5], b[5];
int main(){
    scanf("%s %s", a,b);
    swap(a);
    swap(b);   
    for(int i=0;i<3;i++){
        if(a[i]>b[i]){
            printf("%s", a);
            break;
        }
        else if(a[i]<b[i]){
            printf("%s", b);
            break;
        }
        else continue;
    }
    return 0;
}
char swap(char ary[]){
    char temp;
    temp = ary[0];
    ary[0] = ary[2];
    ary[2] = temp; 
}