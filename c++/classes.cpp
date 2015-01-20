#include <iostream>
#include <string>
using namespace std;

class test
{
	private:

		string text;
		int number;

	public:
		test()
		{
			text = "static class";
		}
		
		void conf(int num, int nr = 1)
		{
			number = num * nr;
		}

		void print()
		{
			cout << text << ": " << number << "\n";
		}
};

class test2
{
	private:

		int number0, number1;

	public:
		
		test2(int x, int y)
		{
			number0 = x;
			number1 = y;
		}

		void print()
		{
			cout << "new class: " << number0 + number1 << "\n";
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
	
	test2 *pat3;
	
	pat3 = new test2(120, 80);
	(*pat3).print();
	
}