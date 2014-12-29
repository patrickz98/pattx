#include <stdio.h>
#include <string.h>

int main()
{
	char satz[10];
	char test[20];

	printf("\n## 1 ## Bitte einen Satz eingeben: ");
    scanf("%9s", satz);
	printf("## 1 ## Eingabe: %s\n", satz);

// 	fgets(satz, 9, stdin);
    fflush(stdin);

	printf("\n## 2 ## Bitte einen Satz eingeben: ");
	scanf("%19s", test);
	printf("## 2 ## Eingabe: %s\n", test);

// 	fgets(test, 19, stdin);
	fflush(stdin);

	return 0;
}
