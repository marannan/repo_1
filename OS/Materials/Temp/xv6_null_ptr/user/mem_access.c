#include "types.h"
#include "stat.h"
#include "user.h"

int main(int argc, char *argv[])
{
 	char *ptr = (char *) ((640*1024) - 4096);

	printf(1,"%x\n", ptr);

	*ptr = 'a';

	printf(1,"%c\n", *ptr);

  	exit();
}
