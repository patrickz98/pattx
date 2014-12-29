#include <stdio.h>
#include <string.h>

int main()
{
	int i = 0;
	char satz[10];

	printf("\nBitte einen Satz eingeben: ");
    scanf("%9c", satz);
    fflush(stdin);
	
	printf("Eingabe: %s\n", satz);
	printf("Der Satz besteht aus %lu Zeichen\n", strlen(satz));

	while (satz[i] != '\0')
	{
		printf("%c", satz[i]);
		i++;
	}
	printf("\nSatz[5] enthält eine null\n");
	satz[5] = '\0';

	printf("Der Satz besteht aus %lu Zeichen\n\n", strlen(satz));

	return 0;
}
