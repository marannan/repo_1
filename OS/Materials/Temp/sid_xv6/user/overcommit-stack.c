#include "types.h"
#include "stat.h"
#include "user.h"

void f(int a) 
{
    printf(1, "A: %d : %x \n", a, &a);

    f(++a);
}

int main(int argc, char **argv)
{
    printf(1, "OVERCOMMIT STACK TEST \n");
    f(1);
    printf(1, "DONE");

    return 0;
}
