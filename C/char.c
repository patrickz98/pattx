#include <stdio.h>
#include <ctype.h>

int main()
{
	char eingabe;
	int zahl;

	printf("eingabe: %c zahl: %i\n", eingabe, zahl);
	printf("(O)ktal, (H)ex oder (A)SCII\n");
	
	eingabe = getchar();
	printf("Zahl eingeben: ");
	scanf("%i", &zahl);
	
	switch(toupper(eingabe))
	{
		case 'O':
			printf("Dezimal %i = Oktal %o \n", zahl, zahl);
			break;
		case 'H':
			printf("Dezimal %i = Hex %x \n", zahl, zahl);
			break;
		case 'A':
			if (zahl <= 255)
			{
				printf("ASCII-code %i = %c \n", zahl, zahl);
			}
			else
			{
				printf("Zahl zu gross ! \n\a");
			}
			break;

	}
	
	return 0;
}