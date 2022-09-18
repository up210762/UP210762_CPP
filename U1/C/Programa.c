#include <stdio.h>
#include <stdlib.h>

int main()
{
    float a, b, c;
    int e;
    printf("Calculadora de prueba");
    printf("\n\n¿Qué operación deseas realizar?\n\n");
    printf("1) Suma\n2) Resta\n3) Multiplicación\n4) División\n\n");
    scanf("%d", &e);
    if (e == 1)
    {
        printf("Escribe el primer número: ");
        scanf("%f", &a);
        printf("¿Cuánto quieres sumar?\n> ");
        scanf("%f", &b);
        c  = a + b;
        printf("El resultado de la suma es: %f", c);
    }
    if (e == 2)
    {
        printf("Escribe el primer número: ");
        scanf("%f", &a);
        printf("¿Cuánto quieres restar?\n> ");
        scanf("%f", &b);
        c = a - b;
        printf("El resultado de la resta es: %f", c);
    }
    if (e == 3)
    {
        printf("Escribe el primer número a multiplicar\n> ");
        scanf("%f", &a);
        printf("¿Por cuánto lo quieres multiplicar?\n> ");
        scanf("%f", &b);
        c = a + b;
        printf("El resultado de la multiplicación es: %f", c);
    }
    if (e == 4)
    {
        printf("Escribe el primer número a dividir\n> ");
        scanf("%f", &a);
        printf("¿Entre cuánto quieres dividir?\n> ");
        scanf("%f", &b);
        c = a / b;
        printf("El resultado de la división es: %f", c);
    }
}