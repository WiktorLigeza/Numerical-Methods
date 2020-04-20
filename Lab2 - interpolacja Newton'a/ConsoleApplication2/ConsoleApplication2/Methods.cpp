#include "H.h"

///Loads data from txt file
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

double *Interpol::ComputeQuotient()
{
	int r = size;
	double z;

	for (int j = 0; j < r - 1; j++)
	{
		for (int i = r - 1; i > j; i--)
		{
			y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j - 1]);
		}
	}
	return y;
}

double Interpol::Newton(double* p, int arg)
{
	int r = size;
	double w;
	double sum = 0;
	int j, i;
	for (i = r - 1; i >= 0; i--)
	{
		w = 1;
		for (j = 0; j < i; j++)
			w *= (arg - x[j]);

		w *= p[j];
		sum += w;
	}

	for (int i = 0; i < r; i++)
	{
		cout << y[i] << endl;
	}


	return sum;
}


