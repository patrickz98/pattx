#include <stdio.h>
#include <string.h>

int main()
{
	char satz[10];
	char test[20];

	printf("\n## 1 ## Bitte einen Satz eingeben: ");
    scanf("%9s", satz);
    fflush(stdin);
// 	fgets(satz, 9, stdin);

	printf("## 1 ## Eingabe: %s\n", satz);


	printf("\n## 2 ## Bitte einen Satz eingeben: ");
	scanf("%19s", test);
	fflush(stdin);
// 	fgets(test, 19, stdin);

	printf("## 2 ## Eingabe: %s\n", test);


	return 0;
}
