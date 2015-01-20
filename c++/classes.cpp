#include <iostream>
#include <string>
using namespace std;

class test
{
	private:
		string test = "test class";
		int number;
	public:
		
		void conf(int num, int nr = 1)
		{
			number = num * nr;
		}

		void print()
		{
			cout << test << ": " << number << "\n";
		}
};

int main()
{
	cout << "classes\n\n";

	test pat1, pat2;
	
	pat1.conf(2, 12045);
	pat2.conf(100);
	
	pat1.print();
	pat2.print();
}