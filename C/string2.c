#include <stdio.h>
#include <string.h>

int main()
{
	char satz[10];
	char test[20];

	printf("\n## 1 ## Bitte einen Satz eingeben: ");
    scanf("%9s", satz);
// 	fgets(satz, 9, stdin);

	printf("## 1 ## Eingabe: %s\n", satz);
    fflush(stdin);

	printf("\n## 2 ## Bitte einen Satz eingeben: ");
	scanf("%19s", test);
// 	fgets(test, 19, stdin);

	printf("## 2 ## Eingabe: %s\n", test);
	fflush(stdin);

	return 0;
}
