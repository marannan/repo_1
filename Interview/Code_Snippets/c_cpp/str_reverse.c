#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int hash_table[256] = {0};
char str[256];
char rev_str[256];

debug(char *str)
{
	//printf("%s\n", str);
	return;
}

void str_reverse_2(char *in_str)
{
	char *start = in_str;
    char *end = in_str + strlen(in_str) - 1;
    char temp;

    while(end > start)
    {
    	temp = *end;
    	*end = *start;
    	*start = temp;

    	start++;
    	end--;
    }

}

char* str_reverse(const char *in_str)
{
	if (str == 0)
    {
    	printf("null input\n");
    	exit(1);
    }

    /* skip empty string */
    if (*str == 0)
    {
    	return "";
    }

	int in_str_len = strlen(in_str);
	int i = 0;

	sprintf(str,"in str: %s len: %d",in_str, in_str_len);
	debug(str);

	while(in_str_len > 0)
	{
		rev_str[i++] = in_str[--in_str_len];
	}
	rev_str[i] = '\0';

	sprintf(str,"rev str: %s len: %d",rev_str, (int)strlen(rev_str));
	debug(str);

	return rev_str;
}

int main(int argc, char *argv[])
{
	if(argc == 2)
	{
		str_reverse_2(argv[1]);
		printf("rev str: %s\n", argv[1]);
	}

	else
		printf("error: argument\n");	
	
	return 0;
}