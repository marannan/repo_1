#include "types.h"
#include "stat.h"
#include "user.h"

int main(int argc, char **argv)
{
    int *p = NULL;
    printf(1, "NULL PTR TEST \n");
    printf(1, "NULL PTR DEREF: %x \n", *p);

    return 0;
}
