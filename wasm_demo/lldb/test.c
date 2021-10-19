#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char str[8] = "dog";
    printf("ptr of str is %p\n", str);

    char *arr = (char *)malloc(16);
    strcat(arr, str);
    printf("%s\n",arr);
    printf("ptr of arr is %p\n", arr);
    
    
    scanf("%s", str);

    return 0;
}

