#include "types.h"
#include "stat.h"
#include "user.h"

#define PGSIZE 4096

int main(int argc, char **argv)
{
    printf(1, "OVERCOMMIT HEAP TEST \n");
    int i = 0;
    while(1) {
        i++;
        printf(1, "Count: %d \n", i);
        if(malloc(PGSIZE) == NULL)
            break;
    }
    printf(1, "DONE \n");

    return 0;
}
