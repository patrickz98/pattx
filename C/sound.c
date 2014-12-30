#include <stdio.h>

int main()
{
	int zahl = 0;

	while (zahl < 8)
	{
		printf("%d\a", zahl);
		zahl++;
//		sleep(1);
	}
	
	return 0;
}
