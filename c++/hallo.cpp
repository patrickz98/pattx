#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	cout << "hallo Welt\n";

	cout << "stdout: cout\n";
	cerr << "stderr: cerr\n";

	std::fprintf(stdout, "stdout: fprintf\n");
	std::fprintf(stderr, "stderr: fprintf\n");
}
