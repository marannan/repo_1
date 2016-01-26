#include<stdio.h>
#include<stdlib.h>

int *arrayA;//[100];


void nBits(int n1, int n2)
{
	//printf("%d\n",arrayA[0]);
	if(n1 <= 0)
	{
		for(int i=0; i<n2; i++)
			printf("%d", arrayA[i]);
		printf("\n");
	}

	else
	{
		arrayA[n1-1] = 0;
		nBits(n1-1,n2);
		arrayA[n1-1] = 1;
		nBits(n1-1,n2);
	}
}

int main(int argc, char* argv[])
{
	int n = atoi(argv[1]);
	printf("n = %d\n",n);
	arrayA = (int *)malloc(sizeof(int)*n);
	// arrayA[0] = 0;
	// printf("%d\n",arrayA[0]);
	nBits(n,n);
	return 0;

}