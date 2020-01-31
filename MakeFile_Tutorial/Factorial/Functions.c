#include <stdio.h>
#include "Functions.h"

void print_message(char* ptr)
{
	printf("%s\n", ptr);
}

int fact_func(int number)
{
	if (number <= 1)
	{
		return 1;
	}
	else
	{
		return number * fact_func(number - 1);
	}
}	

