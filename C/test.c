#include <stdio.h>

void test()
{
	int bla = 1233456;
	printf("%d\n", bla);
}

int test2()
{
	int bla = 987654321;
	return bla;
}

int main()
{
	printf("halo\n");
	test();

	printf("%d\n", test2());

	return 0;
}
