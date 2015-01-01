#include <unistd.h>
#include <stdio.h>

int main()
{
	printf("Sleep, good night\a\n");
	sleep(2);
	printf("Wake up\n");

	return 0;
}