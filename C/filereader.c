#include <stdio.h>

int main()
{
	char ch;
	FILE *fp;
	fp = fopen("bla.txt", "r");
	
	while((ch = fgetc(fp)) != EOF)
	{
		printf("%c",ch);
 	}
 	
	fclose(fp);
	
	return 0;
}