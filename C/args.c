#include <stdio.h>

int main(int argc, char *argv[])
{
	printf( "args --> %i \n", argc );
	for (int x = 0; argc > x; x++)
	{
		printf( "you say %s \n", argv[x] );
	}
}
