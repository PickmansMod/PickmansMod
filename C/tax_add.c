#include <stdio.h>

int main(void)
{
    float tax, amount, tax_added;
    
    printf("Enter an amount: ");
    scanf("%f", &amount);
    printf("Enter the tax: ");
    scanf("%f", tax);
    tax_added = amount + amount * (tax / 100);
    printf("With tax added: ", tax_added);
    return 0;
}