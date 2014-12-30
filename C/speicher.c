#include <stdio.h>

void data(int *adr)
{
	*adr = 88;
}

int main()
{
	int var = 10;
	int *var2 = &var;

    printf("0 --> %u\n", var2);
    printf("0 --> %d\n", *var2);


	printf("1 --> %d\n", var);
    printf("1 --> %u\n", &var);

	data(&var);

	printf("2 --> %d\n", var);
    printf("2 --> %u\n", &var);

	return 0;
}
