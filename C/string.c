#include <stdio.h>
#include <string.h>

int main()
{
	int i = 0;
	char satz[10];
	char test[20];

	printf("Bitte einen Satz eingeben: ");
	scanf("%10s", &satz);
	printf("Eingabe: %s\n", satz);
	printf("Der Satz besteht aus %lu Zeichen\n", strlen(satz));

 	printf("Test: ");
 	scanf("%20s", &test);

	while (satz[i] != '\0')
	{
		printf("%c", satz[i]);
		i++;
	}
	printf("\nSatz[5] enthält eine null\n");
	satz[5] = '\0';
	printf("Der Satz besteht aus %lu Zeichen\n", strlen(satz));

	return 0;
}
