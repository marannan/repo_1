#include "types.h"
#include "stat.h"
#include "user.h"

int main(int argc, char **argv)
{
    int i;
    printf(1, "MALLOC TEST \n");
    int *a = (int*) malloc(sizeof(int) * 10);
    for (i = 0; i < 10; i++)
        a[i] = i;
    for (i = 0; i < 10; i++)
        printf(1, "A[%d] = %d : %x \n", i, a[i], &a[i]);

    int *b = (int*) malloc(sizeof(int) * 50);
    for (i = 0; i < 50; i++)
        b[i] = i;
    for (i = 0; i < 50; i++)
        printf(1, "B[%d] = %d : %x \n", i, b[i], &b[i]);

    int *c = (int*) malloc(sizeof(int) * 100);
    for (i = 0; i < 100; i++)
        c[i] = i;
    for (i = 0; i < 100; i++)
        printf(1, "C[%d] = %d : %x \n", i, c[i], &c[i]);

    printf(1, "DONE \n");
    return 0;
}
