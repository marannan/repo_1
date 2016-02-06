#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int foo(int a, int b)
{
	return a+b;
}

int main(int argc, char *argv[])
{
	int a = 2;
	int b = 2;
	int (*c)(int,int);
	int d = 0;

	c = &foo; // or c = foo;

	d = c(a,b);

	printf("%d\n",d);

	return 0;
}