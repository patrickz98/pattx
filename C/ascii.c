#include <stdio.h>

int main()
{
	char eingabe;
	int zahl;

	printf("eingabe: %c zahl: %i\n", eingabe, zahl);
	for (zahl = 0; zahl <= 255; zahl = zahl + 1)
	{
		printf("ASCII-code %i = %c \n", zahl, zahl);
	}

	return 0;
}