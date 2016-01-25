#include "types.h"
#include "stat.h"
#include "user.h"
#include "fs.h"
#include "fcntl.h"
#include "syscall.h"
#include "traps.h"

int stdout = 1;

int main(int argc, char *argv[])
{

  int no = getsyscallnumtotal();
  printf(stdout, "no of process: %d \n", no);
  exit(); 


}
