#include "types.h"
#include "stat.h"
#include "user.h"

int main(int argc, char **argv)
{
    int a[10] = {0};
    int i;

    for (i = 0; i < 10; i++)
        a[i] = i;
    for (i = 0; i < 10; i++)
        printf(1, "A[%d] = %d : %p \n", i, a[i], &a[i]);

    printf(1, "DONE \n");

    return 0;
}
