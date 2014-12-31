#include <stdio.h>
#include <string.h>
int main()
{
	char satz[10];
	char test[20];

	printf("\n## 1 ## Bitte einen Satz eingeben: ");
	scanf("%9s", satz);
//  fgets(satz, 9, stdin);
	fflush(stdin);

	printf("## 1 ## Eingabe: %s\n", satz);
	printf("## 1 ## besteht aus %lu Zeichen\n", strlen(satz));
	printf("\n## 2 ## Bitte einen Satz eingeben: ");
	scanf("%19s", test);
//  fgets(test, 19, stdin);

	fflush(stdin);

	printf("## 2 ## Eingabe: %s\n", test);
	printf("## 2 ## besteht aus %lu Zeichen\n", strlen(test));

	return 0;
}
