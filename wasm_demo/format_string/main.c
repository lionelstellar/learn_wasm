#include <stdio.h>
#include <stdlib.h> 
#include <emscripten.h>
int main(int argc, const char *argv[]) { 
    // char bof[] = "AAAA"; 
    // printf("%x.%x.%x.%x.%x.%x.%x.%x.%x.\n");
    char bof[] = "\x01"; 
    printf("%x.%x.%x.%x.%n.\n");
    return 0; 
}