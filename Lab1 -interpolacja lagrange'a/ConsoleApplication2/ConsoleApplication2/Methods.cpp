#include "H.h"


void Interpol::Load()
{
	fstream plik;

	plik.open("DATA.txt");
	plik >> size;

	 x = new double[size];
	 y = new double[size];

	//load
	cout << "x:";
	for (int j = 0; j < size; j++)
	{
		plik >> x[j];
		cout <<" "<<x[j];
	}
	cout << endl;

	cout << "y:";
	for (int j = 0; j < size; j++)
	{
		plik >> y[j];
		cout <<" "<< y[j];
	}
	cout << endl;

}

double Interpol::Compute( int r)
{
	double a = 0;
	double b;

	for (int c = 0; c < size; c++)
	{
		b = 1;
		for (int d = 0; d < size; d++)
		{
			if (d != c)
			{
				b = b * ((r - x[d]) / (x[c] - x[d]));
			}
		}
		a += b * y[c];
	}
	return a;
}

