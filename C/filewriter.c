#include <stdio.h>

int main()
{
	char ch;
	FILE *fp;
	fp = fopen("xxx.txt", "w");
	
 	fprintf(fp, "askjdfhkjashdfkhaskjh");

	fclose(fp);
	
	return 0;
}