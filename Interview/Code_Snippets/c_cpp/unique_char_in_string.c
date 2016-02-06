#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int hash_table[256] = {0};
char str[256];

debug(char *str)
{
	//printf("%s\n", str);
	return;
}

int put(int hash_val)
{
	sprintf(str,"hash_val: %d\n",hash_val);
	debug(str);

	hash_table[hash_val] = hash_table[hash_val] + 1;
	sprintf(str,"hash_table[%d]: %d\n",hash_val, hash_table[hash_val]);
	debug(str);

	if(hash_table[hash_val] > 1)
		return -1;

	return 0;
}

int main(int argc, char *argv[])
{

	int i = 0;
	int str_len = 0;
	int hash_val;

	for(i = 0; i < strlen(argv[1]); i++)
	{
		hash_val = argv[1][i] % 256 ;
		if(put(hash_val) != 0)
		{
			printf("no\n");
			exit(0);
		}
	}

	printf("yes\n");
	return 0;
}