#include "types.h"
#include "stat.h"
#include "user.h"

int main(int argc, char **argv)
{
    //char *p = (char*) 0x7D000;
    char *p = (char*) 0xF4C00;
    printf(1, "P -> %x: %c \n", p, *p);
    return 0;
}
