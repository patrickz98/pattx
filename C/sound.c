#include <stdio.h>

int main()
{
	char eingabe;
	int zahl = 0;

	printf("eingabe: %c zahl: %i\n", eingabe, zahl);

	while (zahl < 100)
	{
		eingabe = getchar();
		printf("%c\n\a", eingabe);
		zahl++;
	}
	
	return 0;
}