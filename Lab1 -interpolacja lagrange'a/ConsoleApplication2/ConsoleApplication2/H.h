
#include <iostream>
#include <fstream>

using namespace std;

class Interpol
{
public:

	int size;
	double* x;
	double* y;

	//methods
	double Compute( int );
	void Load();

	

};