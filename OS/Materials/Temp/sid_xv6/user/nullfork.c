// Test fork + nullptr
#include "types.h"
#include "stat.h"
#include "user.h"

int
main(int argc, char **argv)
{
    int pid = getpid();
    if (fork() == 0) {
        char *p = NULL;
        printf(1, "Child: Null Ptr Deref Test");
        printf(1, "%x %c", p, *p);

        printf(1, "Should Never Reach Here!!");
        kill(pid);
        exit();
    }
    else {
        printf(1, "Parent: Waiting for Child to die!");
        wait();
    }
    return 0;
}
