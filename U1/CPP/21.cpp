#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int fin,pinta,num,suma,pc_num,pc;
    srand(time(NULL));
    printf("bienvenido al juego de 21 y las cartas deben ser igual o menor a 21,\n");
    printf("si la computadora es mayor que la computadora ganas!!!,\n");
    printf("pero si sobrepasa a 21 pierde inmediatamente,\n");
     fin = 0;
     suma = 0;
     while (fin!=2)
     {
        num=(rand()%10)+1;
        printf("%d",num);
        pinta = (rand()%4)+1;
        if (pinta==1)
        {
            printf(" de Oro\n\n");
        }
        if (pinta==2)
        {
            printf(" de bastones\n\n");
        }
        if (pinta==3)
        {
            printf(" de copas\n\n");
        }
        if (pinta==4)
        {
            printf(" de espadas\n\n");
        }
        suma = suma + num;
        printf("LA SUMA ES DE: %d\n\n", suma);
        printf("Desea pedir otra carta? \nSI>>marque 1 \nNO>>marque 2\n\n");
        scanf("%d",&fin);
        if (suma>21)
        {
            printf("Ha perdido el juego!\nLa suma excede los 21\n\n");
            fin = 2;
        }
     }
     pc = (rand()%7)+1;
     pc_num = pc + 16;

     if (pc_num>21)
     {
        printf("puntaje: %d\nPUNTAJE PC: %d\n" ,suma,pc_num);
        printf("HA GANADO!!!\n\n");
     }
     else if (suma<=21)
     {
        if (suma>pc_num)
        {
            printf("puntaje: %d\nPUNTAJE PC: %d\n" ,suma,pc_num);
            printf("HA GANADO!!!\n\n");
        }
        if (suma==pc_num)
        {
            printf("puntaje: %d\nPUNTAJE PC: %d\n" ,suma,pc_num);
            printf("EMPATE?\n\n");
        }
        if (suma<pc_num)
        {
            printf("puntaje: %d\nPUNTAJE PC: %d\n" ,suma,pc_num);
            printf("HA PERDIDO\n\n");
        }
     }

     system("pause");

}
