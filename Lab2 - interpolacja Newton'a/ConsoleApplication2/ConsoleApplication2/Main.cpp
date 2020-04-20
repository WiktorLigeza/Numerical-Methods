
#include "H.h"

int main()
{
    int R;
    Interpol i;
    i.Load();
    cout << "podaj w ktorym miejscu szukasz wartosc, x = ";
    cin >> R;
    double* b = i.ComputeQuotient();
    cout<<"wartosc wynosi w x "<< i.Newton(b,R);

}





