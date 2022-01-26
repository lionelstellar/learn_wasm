#include <stdio.h>
int main(){
    FILE *f = fopen("file.txt", "a");
    fprintf(f, "Append Constant Text.");
    fclose(f);
    return 0;
}