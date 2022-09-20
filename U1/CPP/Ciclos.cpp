#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n = 0, i, par, impar;
    for (int i = 1; i <= 10; i++)
    {
        /* code */
        if (i == 3)
            printf("No se puede imprimir   ");
        else
            printf("[Contador %d]   ", i);
        n = n + i;
        if (i % 2 == 0)
            par = par + i;
        else
            impar = impar + i;
    }
    printf("\nLa suma de diez núumeros es: %d", n);
    printf("\nLa suma de los números pares es: %d", par);
    printf("\nLa suma de los números impares es: %d", impar);
    return 0;

}