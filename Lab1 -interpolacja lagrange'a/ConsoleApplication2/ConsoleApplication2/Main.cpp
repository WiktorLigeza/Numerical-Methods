
#include "H.h"

int main()
{
    int R;
    Interpol i;
    i.Load();
    cout << "podaj w ktorym miejscu szukasz wartosc, x = ";
    cin >> R;
    cout<<"wartosc wynosi: "<< i.Compute(R);

}







