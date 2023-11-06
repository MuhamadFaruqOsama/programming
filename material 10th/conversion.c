// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    printf("\a");
    printf("This\b\b\b ia a text\n");
    printf("\75\n"); /* The hexadecimal number 75 correspondes to the '=' character */
    printf("This\tis\ta\x9text\n"); /* The hexadecimal number 9 corresponds to the horizontal tab. */
    printf("This is a \"text\'\n");
    printf("This is a \\text\\\n");
    printf("Sample\rtext\n");
    
    return 0;
}