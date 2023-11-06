// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    float a = 1.2365;
    
    printf("%f\n", a);
    printf("%.2f\n", a);
    printf("%.*f\n", 3, a);
    printf("%.f\n", a);
    
    return 0;
}