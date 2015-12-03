#include "types.h"
#include "stat.h"
#include "user.h"

void a(void);
void b(void);
void c(void);
void d(void);

int main(int argc, char **argv)
{
    printf(1, "Starting STACK-GROWTH \n");
    a();
    printf(1, "DONE \n");

    return 0;
}

void a(void)
{
    printf(1, "begin: A \n");
    int a[250] = {0};
    int i;

    for (i = 0; i < 250; i++)
        a[i] = i;
    for (i = 0; i < 250; i++)
        printf(1, "A[%d] = %d : %p \n", i, a[i], &a[i]);

    printf(1, "end: A \n");
    b();
}

void b(void)
{
    printf(1, "begin: B \n");
    int b[250] = {0};
    int i;

    for (i = 0; i < 250; i++)
        b[i] = i;
    for (i = 0; i < 250; i++)
        printf(1, "B[%d] = %d : %p \n", i, b[i], &b[i]);

    printf(1, "end: B \n");
    c();
}

void c(void)
{
    printf(1, "begin: C \n");
    int c[250] = {0};
    int i;

    for (i = 0; i < 250; i++)
        c[i] = i;
    for (i = 0; i < 250; i++)
        printf(1, "C[%d] = %d : %p \n", i, c[i], &c[i]);

    printf(1, "end: C \n");
    d();
}

void d(void)
{
    printf(1, "begin: D \n");
    int d[250] = {0};
    int i;

    for (i = 0; i < 250; i++)
        d[i] = i;
    for (i = 0; i < 250; i++)
        printf(1, "D[%d] = %d : %p \n", i, d[i], &d[i]);

    printf(1, "end: D \n");
}
