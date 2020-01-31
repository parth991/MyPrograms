#include <stdio.h>
#include <stdlib.h>
#include "Functions.h"

int main(int argc, char* argv[])
{
	int factorial = 0;
	print_message("Let the fun begin");
	factorial = fact_func(10);
	printf("%d\n", factorial);
	return 0;
}
