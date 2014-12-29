#include <stdio.h>

int main()
{
	int zahl = 0;

	while (zahl < 100)
	{
		printf("%d\n\a", zahl);
		zahl++;
		sleep(1);
	}
	
	return 0;
}
