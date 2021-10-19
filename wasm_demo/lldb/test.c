#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    // stack
    char str[16] = "AAAAAAAAAAAAAAA";
    printf("STACK DATA:%s\n",str);
    printf("ptr of STACK str is %p\n", str);


    // heap
    char *arr = (char *)malloc(16);
    arr = "BBBBBBBBBBBBBBB";
    printf("HEAP DATA:%s\n",arr);
    printf("ptr of HEAP arr is %p\n", arr);
    
    
    scanf("%s", str);

    return 0;
}

