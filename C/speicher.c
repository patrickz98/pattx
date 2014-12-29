#include <stdio.h>

void data(int *adr)
{
	*adr = 88;
}

int main()
{
	int var = 10;
	int *var2 = &var;

	printf("1 --> %d\n", var);
    printf("1 --> %d\n", &var);

	data(&var);

	printf("2 --> %d\n", var);
    printf("2 --> %d\n", &var);

	return 0;
}
