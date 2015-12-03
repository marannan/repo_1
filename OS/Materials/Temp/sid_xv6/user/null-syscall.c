#include "types.h"
#include "stat.h"
#include "user.h"

int main(int argc, char **argv)
{
    printf(1, "NULL SYSCALL TEST \n");
    int fd;
    fd = open(NULL, 0);
    if (fd < 0) {
        printf(1, "error! \n");
    }
    printf(1, "DONE \n");

    return 0;
}
