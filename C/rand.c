#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int i;
    time_t t;

    time(&t);
    srand((unsigned int)t);              /* Zufallsgenerator initialisieren */

	printf("Time: %u\n", (unsigned int)t);

    for ( i=0; i<20; i++ )
	{
    	printf("%d ", rand() % 6 + 1);     /* Wuerfeln */
	}

    printf("\n");
}
