//#include <windows.h>
#include <iostream>
using namespace std;
/*
void clrscr() {
    HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD coord = {0, 0};
    DWORD count;
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(hStdOut, &csbi);
    FillConsoleOutputCharacter(hStdOut, ' ', csbi.dwSize.X * csbi.dwSize.Y,
                               coord, &count);
    SetConsoleCursorPosition(hStdOut, coord);
}
void gotoxy(int x, int y) {
    HANDLE hconsola;
    COORD Wpos;
    Wpos.X = x;
    Wpos.Y = y;
    hconsola = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(hconsola, Wpos);
}
*/

//  Linux    system("clear")
void gotoxy(int x, int y) {
    // Coloca el cursor en la posicion (x,y)
    cout << "\033[" << y << ";" << x << "f";
}


void signo_gato() {
    system("clear");
    int n = 1;
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            gotoxy(12+j*4, 7+i*3); cout << n ;
            n = n + 1;
        }
    }
    for (int i = 0; i <= 1; i++) {
        gotoxy( 11 , 9+i*3 ); cout << "---|---|---" ;
    }
    for (int i = 0; i <=7; i++)  {
        gotoxy( 14, 7+i ); cout << "|" ;
        gotoxy( 18, 7+i ); cout << "|" ;
    }

}

int main(int argc, char const *argv[]) {
    system("clear");
    // clrscr();
    signo_gato();
    gotoxy(1,20); cout << "\n. . . Hecho" << endl;
    return 0;
}
