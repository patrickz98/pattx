#include <iostream>
using namespace std;

int main()
{
	cout << "hallo Welt\n";
	
	cout << "stdout: cout\n";
	cerr << "stderr: cerr\n";

	fprintf(stdout, "stdout: fprintf\n");
	fprintf(stderr, "stderr: fprintf\n");
}