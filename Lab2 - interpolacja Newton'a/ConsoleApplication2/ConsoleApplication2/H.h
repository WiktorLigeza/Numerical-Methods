
#include <iostream>
#include <fstream>

using namespace std;

class Interpol
{
public:

	int size;
	double* x;
	double* y;
	double* k;

	//methods
	void Load();
	double* ComputeQuotient();
	double Newton(double*, int);
	

};